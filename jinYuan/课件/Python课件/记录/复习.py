#coding:gbk

#python 模块
    #time datetime calendar  （http://www.cnblogs.com/qq78292959/archive/2013/03/22/2975786.html）
        #time.time()  当前时间（当前时区，返回一个就元素元祖）
        #time.localtime()      本地时间
        #time.gmtime()      时间戳时间
        #time.asctime()     0时区时间
        #time.ctime()       将时间戳时间转化为9元素元组时间
        #time.mktime()      将9元素元组时间转化为时间戳时间
        #time.sleep()       延迟时间
        #time.clock()       记录时间
        #time.strftime()    简易查询时间

    #wx     （图形化）                (http://www.tuicool.com/articles/nUfuIjI)
'''
app = wx.App()  实例化一个应用程序
frame = wx.Frame(None)      实例化一个窗口组件，并设定父表
panel = wx.Panel(frame)     设定画布

frame.Show()    开启图形化窗口调整窗口组件的显示功能
app.MainLoop()      开启主循环
'''
        #Frame      窗口
            #parent  id  title  size  pos  style  name
        #Button
            #lable
        #TextCtrl
            #value
            #style
                #wx.HSCROLL
                #wx.TE_MULTILINE

        #尺寸器布局
            #panel
            #创建尺寸器
                #BoxSizer
                    #wx.VERTICAL
            #添加组件
                #Add
                    #name
                    #proportion
                    #flag
                        #wx.EXPAND 样式
                        #方向
                            #wx.ALL
                            #wx.TOP
                            #wx.BOTTOM
                            #wx.LEFT
                            #wx.RIGHT
            #声明主尺寸器
                #SetSizer

        #绑定事件
            #Bind
            #事件函数
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
        #服务端
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
                #新的套接字对象
                    #TCP
                        #send  sendall
                        #recv()
                    #UDP
                        #sendto
                        #recvfrom
                #客户端的身份

            #close()

        #客户端
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
        #先进先出  Queue.Queue(maxsize)
        #先进后出  Queue.LifoQueue(maxsize)
        #优先级别低的先出  Queue.PrioorityQueue(maxsize)
        #put 向队列中添加
        #get 获取队列中的对象
        #full 判断队列内的对象数量是否达到最大值
        #empty 判断队列中是否为空
        #qsize 查看当前队列中的对象个数
        #join  将当前队列挂起，待队列操作执行完毕后再进行下一步操作
        

    #urllib urllib2
        #数据获取
            #urlencode()
            #Request(url,data,headers)
            #urlopen(url,data,timeout)
                #read()
        #数据过滤
            #re
            #lxml BeautifulSoup
    
        #数据存储

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
        #.特殊命令
        #sql语句
    
    #logging
        #basicConfig("%(asctime)s %(levelname)s %(message)s")
        #debug  info  warning  error  critical
    
    #re
        #内容匹配
            #匹配的规则
                #匹配内容的规则
                    #原样匹配
                    #.
                    #\W \w
                    #\D \d
                    #\S \s
                    #\B \b
                    #\A \Z  \A 从开始匹配  \Z从末尾匹配
                    #^  $   \^从每一行的开始匹配  $ 从每一行的末尾进行匹配
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
                    
                #匹配数量的规则
                    # *
                    # +
                    # ?
                    # {} {,}
                    
                #特殊规则
                    #re.S   修改'.'的匹配方式，换行符也能被匹配出来
                    #re.M   更改识别模式，在字符串中的换行符也能识别出来，常与多行匹配连用
                    #re.I   忽略字符大小写
                    
            #匹配的方法
                #findall
                #search
                #match
                    #匹配对象
                        #group
                        #groups
                #sub
                #split
                #compile 编译对象（正则模板）
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

#python 文件操作
    #创建文件操作dui象
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
        #write 写字符串
        #writelines 写序列
        #read
        #readline
        #readlines
        #seek
            #0 1 2
        #tell

#python 包机制
    #__init__.py

#python 异常
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

#python 面向对象
    #class Person_Chinese_Bj([继承对象]):
        #域
        #方法(self)
    #实例化

    #三大特征
        #继承
            #经典类继承
            #新式类继承
                #super
        #封装
            #私有化属性
                #__
                #_
        #多态

    #魔术方法
        #__init__   构造函数
        #__del__    析构函数
        #__doc__    说明字符串，将目标中存在的字符串调用出来
        #__dict__   返回一个由类的数据属性组成的字典
        #__module__     查看指定对象的模块
        #__name__   返回指定对象的名字的字符串表现
        #dir    查看指定对象的属性，返回一个由目标是对象的属性名组成的列表
        #hasattr 判断是否有目标属性
        #setattr 设置（修改）目标属性
        #getattr 获得目标属性
        #delattr 删除目标属性

#python 面向过程
    #def fname([arg,...]):
    #函数的调用                                                     
        #fname([arg,...])

    #lambda x,y:x + y

    #return 

'''
zip map input raw_input range xrange open file dir help type len
print list str dict tuple int float long eval ord chr sorted
reversed enumerate next iter repr cmp issubclass isinstance
'''
    #递归
        #最小可能性
        #自身应用自身

    
    #函数的三大器
        #迭代器
            #iter   （next 查看当前函数下的下一个参数）

        #生成器
            #yield  （一种特殊的迭代器）
            
        #装饰器
            #@语法糖   （可以将@后的函数作为一个对象赋值给另一个参数，作为简易的串联）

    #函数作用域
        #L  本地作用域
        #E  （）嵌套作用域
        #G  全局作用域
        #B  內键作用域
        #全局变量   在整体程序中可以被任意函数调用修改的变量
        #局部变量   在一个或几个函数中存在并没有存在与外部的变量。
            #global
    #闭包

#python 语句
    #print
    #exec   执行在'（）内'字符串中的PYTHON语句
    #import
    #赋值语句
    #for循环
        #有循环次数限制
    #while循环
        #无限循环
'''
        while:
            pass
        else:
            pass
'''
        #continue

        #break

    #if判断

    #pass

#python 布尔类型
    #True
    #False
#python数字运算符
    #> < >= <= <> != is == 

#python逻辑运算符
    #and
    #or
    #not

#python 数据类型
    #int
        #双精度
        #单精度
        #long
            #2147483647

    #float

    #str
        #字符串的分片操作

        #特殊字符
            #\n \t \v
        #转义符
            #\ %
        #占位符
            #%s  %d  %f
        #字符串的格式化
            #%
            #format
        #字符串的连接
            #join
            #+
        #字符串切分
            #split
            #rsplit
        #字符串的替换
            #replace
        #字符串的变形
            #upper lower title capitalize swapcase
        #字符串的判断
            #isuppper  islower  istitle
            #isdigit isalnum isalpha
            #startswith  endswith
        #字符串的查找
            #find index count  rfind rindex
        #字符串的编码
            #encode decode
        #字符串的填充
            #zfill center ljust rlust expandtabs
        #字符串的删减
            #strip  lstrip rstrip（删除字符串在打印时的左右两边的空字符串）
#print dir(str)


    #list
        #list  []  range()
        #列表的添加
            #append  insert  extend（将后面的列表中的元素依次添加至前面的列表（类似join））  +
        #列表的删除
            #pop(index) remove(value)
        #列表的查找
            #count index
        #列表的排序
            #sort  reverse

    #tuple
        #单元素元组必须加逗号
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






