#coding:gbk

#python 配置文件
    #.ini  .conf  .py  文本文档
 
import ConfigParser   #python3 configparser

con = ConfigParser.ConfigParser()
con.read('config.ini')
#con.read()
#print con.sections()  #返回指定对象的章节名
#print con.options('HELLO') #返回指定章节下的选项名
#print con.get('HELLO','major') #获取指定章节下选项对应的值
#print con.get('HELLO','gender')
#print con.items('HELLO') #将指定章节下的选项和值合并到一个元组当中，返回列表形式

con.remove_section('XLGameBox')
#print con.sections()
con.remove_option('FunAccelerator','fck')
#print con.options('FunAccelerator')
#con.add_section('PYTHON')
#print con.sections()

#con.add_option('PYTHON','aaa','123')

#con.set('PYTHON','aaa','123') #指定章节下的选项不存在，添加选项和值
#print con.get('PYTHON','aaa')

con.set('HELLO','name','laoli') #指定章节下的选项存在，修改选项对应的值
#print con.get('HELLO','name')

#help(con.write)
#con.write(open('config.ini','w')) #将修好的内容存入配置文件
#con.write(open('hello.ini','a'))
'''
print con.has_section('HELLO')
print con.has_section('XLGameBox')
'''
#print con.has_option('HELLO','ages')




#python 日志
import logging

    #日志等级
        #notset   0
        #debug    10
        #info     20
        #warning  30
        #error    40
        #critical 50


logging.basicConfig(
    filename = 'hello.log',
    format = "[%(asctime)s] [%(levelname)-10s] %(message)s",
    level = 10
)
        
#logging.warning("NameError: name 'dsa' is not defined")
#logging.error("TypeError: unsupported operand type(s) for +: 'int' and 'str'")
#logging.info("My name is ...,my job is ...")

while True:
    try:
        a = 'hello' + input('>>>')
        print a
        logging.info(a)

    except TypeError,e:
        logging.error(e)

    except NameError,e:
        logging.debug(e)
        
    
