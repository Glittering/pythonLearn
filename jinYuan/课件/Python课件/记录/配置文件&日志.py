#coding:gbk

#python �����ļ�
    #.ini  .conf  .py  �ı��ĵ�
 
import ConfigParser   #python3 configparser

con = ConfigParser.ConfigParser()
con.read('config.ini')
#con.read()
#print con.sections()  #����ָ��������½���
#print con.options('HELLO') #����ָ���½��µ�ѡ����
#print con.get('HELLO','major') #��ȡָ���½���ѡ���Ӧ��ֵ
#print con.get('HELLO','gender')
#print con.items('HELLO') #��ָ���½��µ�ѡ���ֵ�ϲ���һ��Ԫ�鵱�У������б���ʽ

con.remove_section('XLGameBox')
#print con.sections()
con.remove_option('FunAccelerator','fck')
#print con.options('FunAccelerator')
#con.add_section('PYTHON')
#print con.sections()

#con.add_option('PYTHON','aaa','123')

#con.set('PYTHON','aaa','123') #ָ���½��µ�ѡ����ڣ����ѡ���ֵ
#print con.get('PYTHON','aaa')

con.set('HELLO','name','laoli') #ָ���½��µ�ѡ����ڣ��޸�ѡ���Ӧ��ֵ
#print con.get('HELLO','name')

#help(con.write)
#con.write(open('config.ini','w')) #���޺õ����ݴ��������ļ�
#con.write(open('hello.ini','a'))
'''
print con.has_section('HELLO')
print con.has_section('XLGameBox')
'''
#print con.has_option('HELLO','ages')




#python ��־
import logging

    #��־�ȼ�
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
        
    
