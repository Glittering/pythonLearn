#coding=UTF-8
import re,urllib,socket,os,datetime,sys,time
from sgmllib import SGMLParser
 
defaultSiteList = ["ZXW","163","RMW","SINA","IFENG"]
argD = os.getcwd()+os.path.sep+'dataNews'
 
 
 
defaultStartTime = "2013-11-02"
defaultEndTime = "2013-11-03"
defaultSockTimeLimit = 20
 
dirForDiv = {'ZXW':['class','left_zw'],'163':['id','endText'],'RMW':['id','p_content'],'SINA':['id','artibody'],'IFENG':['id','main_content']}
#定义从滚动新闻页面提取出新闻Url的正则表达式
dirRegex = {'ZXW':r'<div class=\"dd_bt\"><a href=[^<>]*>[^<>]*</a></div><div class=\"dd_time\">[\d]{2}-[\d]{1,2} [\d]{2}:[\d]{2}</div>','RMW':r'<a href[^<>]*>[^<>]*</a>\[[\d]{2}[^<>]*[\d]{2}:[\d]{2}\]<br>','163':r't\"[^}]*','SINA':r',title[^}]*','IFENG':r'<h4>[\d]{2}/[\d]{2} [\d]{2}:[\d]{2}</h4><a href=[^<>]*>[^<]*'}
class GetNewsParser(SGMLParser):
    """
    继承SGMLParser
    提取出新闻的正文内容
    """
    def __init__(self,site="163"):
        SGMLParser.__init__(self)
        self.site = site
    def reset(self):
        self.newsText = []
        self.flag = False
        self.getdata = False
        self.verbatim = 0
        SGMLParser.reset(self)
         
    def start_div(self,attrs):
        if self.flag == True:
                self.verbatim += 1
                return
 
        for k,v in attrs:
                if k == dirForDiv[self.site][0] and v == dirForDiv[self.site][1]:
                        self.flag = True
                        return
     
    def end_div(self):
        if self.verbatim == 0:
                self.flag = False
        if self.flag == True:
                self.verbatim -= 1
     
    def start_p(self,attrs):
        if self.flag == False:
                return
        self.getdata = True
    def end_p(self):
        if self.getdata:
                self.getdata = False
    def start_script(self,attrs):
        if self.getdata and self.site == "ZXW":
            self.getdata = False
    def handle_data(self,text):
        if self.getdata:
                self.newsText.append(text)
 
class GetChinaNews():
    def __init__(self,str_start_time=defaultStartTime,str_end_time=defaultEndTime,dirName=os.getcwd(),siteList=defaultSiteList,timeLimit=defaultSockTimeLimit):
    #s:str_start_time,e:str_end_time,d:dirName,l:sitelist,t:timeLimit
        self.date_range = self.dateRange(str_start_time,str_end_time)
        self.dir_name = dirName
        self.root_dir_name = dirName
        self.siteList = siteList
        socket.setdefaulttimeout(timeLimit)
        self.strYear = "2013"
        self.strMonth = "11"
        self.strDay = "02"
        self.Url = "This is the roll news page Url."
        self.tag  = 0
         
     
    #set the date range that get news
    def dateRange(self,str_start_time,str_end_time):
        """
        set the date range
        """
        tmp = str_start_time.split('-')
        tmp1 = str_end_time.split('-')
        start_time = datetime.datetime(int(tmp[0]),int(tmp[1]),int(tmp[2]))
        end_time = datetime.datetime(int(tmp1[0]),int(tmp1[1]),int(tmp1[2]))
        for n in range(int((end_time-start_time).days)):
            yield start_time + datetime.timedelta(n)
    def getNewsProperties(self,site,str):
        """
        return the list [newsTitle,newsUrl,newsTime]
        """
        if site == "ZXW" or site == "RMW" or site == "IFENG":
            delimiter = '>'
        else:
            delimiter = '"'
        iList = str.split(delimiter)
         
        if site == "ZXW":
            return [iList[2][:-3],iList[1][9:-1],self.strYear+'-'+self.strMonth+'-'+self.strDay+' '+iList[5].split(' ')[1][:-5]+":00"]
        elif site == "RMW":
            return [iList[1][:-3],iList[0].split(' ')[1][6:-1],re.subn("&nbsp;"," ",self.strYear + '-'+self.strMonth+'-'+self.strDay)[0]]
        elif site == "163":
            return [iList[2],iList[6],iList[10]]
        elif site == "SINA":
            return [iList[1],iList[3],time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(iList[4][-10:])))]
 
        elif site == "IFENG":
            return [iList[3],iList[2].split('"')[1],self.strYear+'-'+self.strMonth+'-'+self.strDay+' '+iList[1][6:11]]
     
    def getNewsFromRollPage(self,site):
        htmlSource = ""
        try:
            sock = urllib.urlopen(self.Url)
            htmlSource = sock.read()
            sock.close()
        except:
            print "Something wrong when openning rollNewsPage:"+self.Url
         
        #solve the 404 problem
        if site == "IFENG":
            NonePattern = re.compile(r"div class=\"mat\"[^>]*")
            if NonePattern.search(htmlSource):
                return False
                 
        m = re.findall(dirRegex[site],htmlSource,re.M)
        newsUrl = "NONE"
        for i in m:
            try:
                 
                newsTitle,newsUrl,newsTime = self.getNewsProperties(site,i)
                #special for ZXW
                if site == "ZXW" and newsUrl[:4] != "http":
                    newsUrl = "http://www.chinanews.com" + newsUrl
                #special for 163 because there are many other days' news on the rollNewsUrl
                if site == "163" and newsTime.split(' ')[0] != self.strYear + '-' + self.strMonth + '-' + self.strDay:
                    continue
                #notconsider the photo news 
                if site == "IFENG" and newsUrl[22:27] == "photo":
                    continue
                sock = urllib.urlopen(newsUrl)
                htmlSource = sock.read()
                sock.close()
                #special for 163: for Pagination news(the news is too long so 163 make it shown in two or more pages)
                if site == "163":
                    allPattern = re.compile(r"_all.html#p1")
                    allUrl = allPattern.search(htmlSource)
                    if allUrl:
                        newsUrl = newsUrl[:-5]+allUrl.group()
                        socks = urllib.urlopen(newsUrl)
                        htmlSource = socks.read()
                        socks.close()
                #newsTime of RMW
                if site == "RMW":
                    pp = re.compile(r'[\d]{2}:[\d]{2}<')
                    RmwTime = pp.search(htmlSource).group()
                    newsTime = newsTime + " " + RmwTime[:-1]+":00"
                     
                #use Parser to get text content of news,stored in strText
                getcontent = GetNewsParser(site)
                getcontent.feed(htmlSource)
                strText = ""
                for k in getcontent.newsText:
                    strText += k
                getcontent.close()
                fileName = site+"-"+str(self.tag)
                self.tag = self.tag + 1
                #store in .txt files
                with open(self.dir_name+fileName+'.txt','w+') as f:
                    f.write(newsTitle+"\n"+newsUrl+"\n"+newsTime+"\n"+strText)
            except KeyboardInterrupt:
                print "Stopped By User."
                sys.exit(0)
            except:
                print "SomethinWrong when getting "+site+" news:"+newsUrl
        return True
 
 
    def getNewsFromSite(self,site): 
         
        self.tag = 0   
        #the rollNewsUrl of every site
        if site == "ZXW":
            self.Url = "http://www.chinanews.com/scroll-news/" + self.strYear + "/" + self.strMonth + self.strDay + "/news.shtml"
            self.getNewsFromRollPage(site)
             
        elif site == "RMW":
            self.Url = "http://people.com.cn/GB/24hour/index" + self.strYear + "_" + self.strMonth + "_" + self.strDay +".html"
            self.getNewsFromRollPage(site)
        elif site == "163":
            self.Url = "http://snapshot.news.163.com/wgethtml/http+!!news.163.com!special!0001220O!news_json.js/"+self.strYear+"-"+self.strMonth+"/"+self.strDay+"/0.js"
            self.getNewsFromRollPage(site)
        elif site == "SINA":
            self.Url = "http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&spec=&type=&date="+self.strYear+"-"+self.strMonth+"-"+self.strDay+"&k=&offset_page=0&offset_num=0&num=30000&asc=&page=1"
            self.getNewsFromRollPage(site)
        elif site == "IFENG":
            pageNum = 1
             
            while pageNum < 1000:#set 1000,the pageNum's max value
                self.Url = "http://news.ifeng.com/rt-channel/rtlist_"+self.strYear+self.strMonth+self.strDay+"/"+str(pageNum)+".shtml"
                if self.getNewsFromRollPage(site) == False:
                    break
                pageNum += 1
        print "Get "+ str(self.tag) + " " + site + " news successfully."
         
    def getChinaNews(self):
        try:
            for tt in self.date_range:
                print "Get News From Date:"+str(tt)
                self.strYear = str(tt.year)
                if tt.month < 10:
                    self.strMonth = "0" + str(tt.month)
                else:
                    self.strMonth = str(tt.month)
                if tt.day < 10:
                    self.strDay = "0" + str(tt.day)
                else:
                    self.strDay = str(tt.day)
                #create folder for the date tt
                self.dir_name = self.root_dir_name + "/"+self.strYear+self.strMonth+self.strDay+"/"
                isExists = os.path.exists(self.dir_name)
                if not isExists:
                    os.mkdir(self.dir_name)
                for i in self.siteList:
                    if i in defaultSiteList:
                        if i == "RMW":
                            socket.setdefaulttimeout(50)
                        self.getNewsFromSite(i)
        except KeyboardInterrupt:
            print "Stopped By User."
            sys.exit(0)
        except:
            print "Somethin wrong when getting chinanews."
#"2013-11-01","2013-12-01",dirName='D:/testnews',timeLimit=20
#s:str_start_time,e:str_end_time,d:dirName,t:timeLimit
argST = defaultStartTime
argED = defaultEndTime
 
argT = defaultSockTimeLimit
args = sys.argv
if not os.path.exists(argD):
    os.mkdir(argD)
 
if len(args) == 1:
    argST = time.strftime('%Y-%m-%d')
    argED = time.strftime('%Y-%m-%d',time.localtime(time.time()+86400))
else:
    if len(args) == 2:
        if args[1] != "-a" and args[1] != "-help":
            print "commond error,please see -help"
            sys.exit(0)
        if args[1] == "-a": 
            argED = time.strftime('%Y-%m-%d',time.localtime(time.time()+86400))
            datetmp = argED.split('-')
            timetmp = time.mktime(datetime.datetime(int(datetmp[0]),int(datetmp[1]),int(datetmp[2])).timetuple())
            argST = time.strftime('%Y-%m-%d',time.localtime(timetmp-86400*30))
        else:
            print "help info of this commond:\nno arg: get news of today\n-a: get recent 30 days' news\n-d 2013-11-01: get news from the day\n-d 2013-11-01 2013-11-02: get news from the begin day to end day\n-dx 2013-11-01 t: get t days' news from the day\n"
            sys.exit(0)
    elif len(args) == 3:
        if args[1] != "-d":
            print "commond error,please see -help"
            sys.exit(0)
        else:
            if not re.match(r"[\d]{4}-[\d]{2}-[\d]{2}$",args[2]):
                print args[2] + " is not a right date format."
                sys.exit(0)
            argST = args[2]
            datetmp = args[2].split('-')
            timetmp = time.mktime(datetime.datetime(int(datetmp[0]),int(datetmp[1]),int(datetmp[2])).timetuple())
            argED = time.strftime('%Y-%m-%d',time.localtime(timetmp+86400))
    elif len(args) == 4:
        if args[1] != "-d" and args[1] != "-dx":
            print "commond error,please see -help"
            sys.exit(0)
        else:
            if not re.match(r"[\d]{4}-[\d]{2}-[\d]{2}$",args[2]):
                print args[2] + " is not a right date format."
                sys.exit(0)
            if args[1] == "-d":
                if not re.match(r"[\d]{4}-[\d]{2}-[\d]{2}$",args[3]):
                    print args[3] + " is not a right date format."
                    sys.exit(0)
                argST = args[2]
                datetmp = args[3].split('-')
                timetmp = time.mktime(datetime.datetime(int(datetmp[0]),int(datetmp[1]),int(datetmp[2])).timetuple())
                argED = time.strftime('%Y-%m-%d',time.localtime(timetmp+86400))
            else:
                if not re.match(r"[\d]*$",args[3]):
                    print args[3] + " is not a right number format."
                    sys.exit(0)
                #download  -dx 2013-11-01 t：
                argST = args[2]
                datetmp = args[2].split('-')
                timetmp = time.mktime(datetime.datetime(int(datetmp[0]),int(datetmp[1]),int(datetmp[2])).timetuple())
                argED = time.strftime('%Y-%m-%d',time.localtime(timetmp+86400*int(args[3])))
                 
G = GetChinaNews(str_start_time=argST,str_end_time=argED,dirName=argD,siteList=defaultSiteList,timeLimit=argT)
G.getChinaNews()        
 
