#coding:gbk

#python ģ��
    #time datetime calendar  ��http://www.cnblogs.com/qq78292959/archive/2013/03/22/2975786.html��
        #time.time()  ��ǰʱ�䣨��ǰʱ��������һ����Ԫ��Ԫ�棩
        #time.localtime()      ����ʱ��
        #time.gmtime()      ʱ���ʱ��
        #time.asctime()     0ʱ��ʱ��
        #time.ctime()       ��ʱ���ʱ��ת��Ϊ9Ԫ��Ԫ��ʱ��
        #time.mktime()      ��9Ԫ��Ԫ��ʱ��ת��Ϊʱ���ʱ��
        #time.sleep()       �ӳ�ʱ��
        #time.clock()       ��¼ʱ��
        #time.strftime()    ���ײ�ѯʱ��

    #wx     ��ͼ�λ���                (http://www.tuicool.com/articles/nUfuIjI)
'''
app = wx.App()  ʵ����һ��Ӧ�ó���
frame = wx.Frame(None)      ʵ����һ��������������趨����
panel = wx.Panel(frame)     �趨����

frame.Show()    ����ͼ�λ����ڵ��������������ʾ����
app.MainLoop()      ������ѭ��
'''
        #Frame      ����
            #parent  id  title  size  pos  style  name
        #Button
            #lable
        #TextCtrl
            #value
            #style
                #wx.HSCROLL
                #wx.TE_MULTILINE

        #�ߴ�������
            #panel
            #�����ߴ���
                #BoxSizer
                    #wx.VERTICAL
            #������
                #Add
                    #name
                    #proportion
                    #flag
                        #wx.EXPAND ��ʽ
                        #����
                            #wx.ALL
                            #wx.TOP
                            #wx.BOTTOM
                            #wx.LEFT
                            #wx.RIGHT
            #�������ߴ���
                #SetSizer

        #���¼�
            #Bind
            #�¼�����
                #event
            #wx.EVT_BUTTON
            #GetValue
            #SetValue
            #write
            #AppendText
                        


    #ConfigParser           ()
        #ConfigParser.ConfigParser()
            #read()
            #sections()
            #options()
            #items()
            #get()
            #remove_section()
            #remove_option()
            #add_section()
            #set()
            #write(open(path,mode))
            #has_option()
            #has_section()


    #lxml
        #etree
            #xpath
                #// 
                #/
                #@
                #position()
                #text()
                #contains(text(),'')
                

    #random
        #random.random()
        #random.choice()
        #random.shuffle()
        #random.randint()
        #random.uniform()
        #random.sample()
        #random.randrange()

    #socket
        #�����
            #socket.socket()
                #family
                    #AF_INET
                    #AF_UNIX
                #type
                    #SOCK_STREAM --> TCP
                    #SOCK_DGRAM  --> UDP

            #bind()

            #listen()

            #accept()
                #�µ��׽��ֶ���
                    #TCP
                        #send  sendall
                        #recv()
                    #UDP
                        #sendto
                        #recvfrom
                #�ͻ��˵����

            #close()

        #�ͻ���
            #socket.socket()
            #connect()
            #send recv
            #close

    #thread
        #start_new_thread()
        #allocate_lock
        #acquire
        #release
        #getName()
        #setName()
        #isAlive()


    #threading
        #Thread
            #start()
            #join()
            #run()
            #__init__()
'''
class Mythread(threading.Thread):
    def __init__(self,arg1,arg1):
        self.arg1 = arg1
        self.arg2 = arg2
        threading.Thread.__init__(self)

    def run(self):
        pass
'''

    #Queue
        #�Ƚ��ȳ�  Queue.Queue(maxsize)
        #�Ƚ����  Queue.LifoQueue(maxsize)
        #���ȼ���͵��ȳ�  Queue.PrioorityQueue(maxsize)
        #put ����������
        #get ��ȡ�����еĶ���
        #full �ж϶����ڵĶ��������Ƿ�ﵽ���ֵ
        #empty �ж϶������Ƿ�Ϊ��
        #qsize �鿴��ǰ�����еĶ������
        #join  ����ǰ���й��𣬴����в���ִ����Ϻ��ٽ�����һ������
        

    #urllib urllib2
        #���ݻ�ȡ
            #urlencode()
            #Request(url,data,headers)
            #urlopen(url,data,timeout)
                #read()
        #���ݹ���
            #re
            #lxml BeautifulSoup
    
        #���ݴ洢

    #os
        #os.remove()
        #os.unlink()
        #os.mkdir
        #os.makedirs()
        #os.chdir()
        #os.listdir()
        #os.chmod()
        #os.rename()
        #os.path
            #os.path.join()

    #sys
        #sys.path
            #sys.path.append()
        #sys.argv
        #sys.stdout
            #sys.stdout.write
        #sys.stdin
        #sys.stderr

    #MySQLdb
        #connect(host,user,passwd,db,charset,port)
        #cursor()
            #execute()
            #executemany()
            #fetchall
            #fetchone
            #fetchmany
        #commit
        #rollback
        #close

    #sqlite3
        #connect(path)
        #sqlite3 hellp.db(hello.sqlite3)
        #.��������
        #sql���
    
    #logging
        #basicConfig("%(asctime)s %(levelname)s %(message)s")
        #debug  info  warning  error  critical
    
    #re
        #����ƥ��
            #ƥ��Ĺ���
                #ƥ�����ݵĹ���
                    #ԭ��ƥ��
                    #.
                    #\W \w
                    #\D \d
                    #\S \s
                    #\B \b
                    #\A \Z  \A �ӿ�ʼƥ��  \Z��ĩβƥ��
                    #^  $   \^��ÿһ�еĿ�ʼƥ��  $ ��ÿһ�е�ĩβ����ƥ��
                    # []
                    # |
                    # [^...]
                    # [...-...]
                    # ()
                    #(?P<name>...)
                    #(?P=name)
                    #(.*) (.*?)
                    #(?=...) (?!...)
                    #(?<=...) (?<!...)
                    #?:
                    
                #ƥ�������Ĺ���
                    # *
                    # +
                    # ?
                    # {} {,}
                    
                #�������
                    #re.S   �޸�'.'��ƥ�䷽ʽ�����з�Ҳ�ܱ�ƥ�����
                    #re.M   ����ʶ��ģʽ�����ַ����еĻ��з�Ҳ��ʶ��������������ƥ������
                    #re.I   �����ַ���Сд
                    
            #ƥ��ķ���
                #findall
                #search
                #match
                    #ƥ�����
                        #group
                        #groups
                #sub
                #split
                #compile �����������ģ�壩
                    #findall
                    #sub
                    #split

    #cgi
        #FieldStorage
            #getvalue
                    
        
    #math
        #sqrt
        #tan
        #sin
        #cos

    #keyword
        #kwlist
        #iskeyword
    #codecs
        #open(path,mode,encode)

#dir
#help

#python �ļ�����
    #�����ļ�����dui��
        #open / file
            #path
            #mode
                #w
                #a
                #r
                #w+ a+ r+
                #rb
                #wb
                #Ua
                #rU
'''
f = open('70.jpg','rb')
print f.read()
f.close()
'''
#zipfile
#tarfile
#reportlab cStringIO
#csv
#xlwt xlrd
#Pillow PIL
        #write д�ַ���
        #writelines д����
        #read
        #readline
        #readlines
        #seek
            #0 1 2
        #tell

#python ������
    #__init__.py

#python �쳣
    #try
    #except
    #Exception

    #try
    #except
    #finally

    #try
    #except
    #else

    #try
    #except
    #else
    #finally

    #raise

#python �������
    #class Person_Chinese_Bj([�̳ж���]):
        #��
        #����(self)
    #ʵ����

    #��������
        #�̳�
            #������̳�
            #��ʽ��̳�
                #super
        #��װ
            #˽�л�����
                #__
                #_
        #��̬

    #ħ������
        #__init__   ���캯��
        #__del__    ��������
        #__doc__    ˵���ַ�������Ŀ���д��ڵ��ַ������ó���
        #__dict__   ����һ�����������������ɵ��ֵ�
        #__module__     �鿴ָ�������ģ��
        #__name__   ����ָ����������ֵ��ַ�������
        #dir    �鿴ָ����������ԣ�����һ����Ŀ���Ƕ������������ɵ��б�
        #hasattr �ж��Ƿ���Ŀ������
        #setattr ���ã��޸ģ�Ŀ������
        #getattr ���Ŀ������
        #delattr ɾ��Ŀ������

#python �������
    #def fname([arg,...]):
    #�����ĵ���                                                     
        #fname([arg,...])

    #lambda x,y:x + y

    #return 

'''
zip map input raw_input range xrange open file dir help type len
print list str dict tuple int float long eval ord chr sorted
reversed enumerate next iter repr cmp issubclass isinstance
'''
    #�ݹ�
        #��С������
        #����Ӧ������

    
    #������������
        #������
            #iter   ��next �鿴��ǰ�����µ���һ��������

        #������
            #yield  ��һ������ĵ�������
            
        #װ����
            #@�﷨��   �����Խ�@��ĺ�����Ϊһ������ֵ����һ����������Ϊ���׵Ĵ�����

    #����������
        #L  ����������
        #E  ����Ƕ��������
        #G  ȫ��������
        #B  �ȼ�������
        #ȫ�ֱ���   ����������п��Ա����⺯�������޸ĵı���
        #�ֲ�����   ��һ���򼸸������д��ڲ�û�д������ⲿ�ı�����
            #global
    #�հ�

#python ���
    #print
    #exec   ִ����'������'�ַ����е�PYTHON���
    #import
    #��ֵ���
    #forѭ��
        #��ѭ����������
    #whileѭ��
        #����ѭ��
'''
        while:
            pass
        else:
            pass
'''
        #continue

        #break

    #if�ж�

    #pass

#python ��������
    #True
    #False
#python���������
    #> < >= <= <> != is == 

#python�߼������
    #and
    #or
    #not

#python ��������
    #int
        #˫����
        #������
        #long
            #2147483647

    #float

    #str
        #�ַ����ķ�Ƭ����

        #�����ַ�
            #\n \t \v
        #ת���
            #\ %
        #ռλ��
            #%s  %d  %f
        #�ַ����ĸ�ʽ��
            #%
            #format
        #�ַ���������
            #join
            #+
        #�ַ����з�
            #split
            #rsplit
        #�ַ������滻
            #replace
        #�ַ����ı���
            #upper lower title capitalize swapcase
        #�ַ������ж�
            #isuppper  islower  istitle
            #isdigit isalnum isalpha
            #startswith  endswith
        #�ַ����Ĳ���
            #find index count  rfind rindex
        #�ַ����ı���
            #encode decode
        #�ַ��������
            #zfill center ljust rlust expandtabs
        #�ַ�����ɾ��
            #strip  lstrip rstrip��ɾ���ַ����ڴ�ӡʱ���������ߵĿ��ַ�����
#print dir(str)


    #list
        #list  []  range()
        #�б�����
            #append  insert  extend����������б��е�Ԫ�����������ǰ����б�����join����  +
        #�б��ɾ��
            #pop(index) remove(value)
        #�б�Ĳ���
            #count index
        #�б������
            #sort  reverse

    #tuple
        #��Ԫ��Ԫ�����Ӷ���
        #count index 

    #dict
        #dict()
        #{}
        #dict(zip())

        #get
        #setdefault
        #update


        #values
        #keys
        #items

        #viewitems
        #viewvalues
        #viewkeys

        #iteritems
        #itervalues
        #iterkeys

        #clear

        #pop(index)
        #popitem()

        #copy

        #has_key  in 

        


#del






