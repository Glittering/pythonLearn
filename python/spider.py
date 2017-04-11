#coding=utf-8
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    #reg = r'data-price="(.+)"'
    reg = r'class="link title" target=".+".+</a>'
    #reg = r'.strong.+ data-price=".+"<em>'
    reg2 = r'<a target.+title="(.+)".+href'
    #reg2 = r'.+title="(.+)".+href'
    imgre = re.compile(reg)
    imgre2 = re.compile(reg2)
    imglist = re.findall(imgre,html)
    imglist2 = re.findall(imgre2,html)
    f=open(r'data.txt','w')
    a = []
    for imgu in imglist:      
        a.append(imgu+'\n')
    f.writelines(a)
    a = []
#    for imgu in imglist2:      
        #imgu = imgu[4:-5]
 #       a.append(imgu+'\n')
 #   f.writelines(a) 
    f.close
    

i=1
#while (i<50 ):
    #url = "https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)+"&trans=1&JL=6_0_0#J_main"
    #html = getHtml(url)
html = getHtml("http://www.toutiao.com/news_tech/")
getImg(html)

