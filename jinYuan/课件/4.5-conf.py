#coding:gbk


import time

'''
def theday(y,m,d):
    thetime = time.mktime((y,m,d,0,0,0,0,0,0))
    now = time.time()
    result = int((now - thetime)/3600/24)
    return result

if __name__ == '__main__':
    thedate = raw_input('Please enter the date:')
    #print thedate
    date_list = thedate.split(thedate[4])
    #y,m,d = date_list
    #print theday(int(y),int(m),int(d))
    
    #y = int(date_list[0])
    #m = int(date_list[1])
    #d = int(date_list[2])
    y,m,d = [int(i) for i in date_list]
    print theday(y,m,d)
    
'''
'''
import time

class OurReader():
    def __init__(self,path):
        self.f = open(path,'r')
        self.f.seek(0,2)
        self.total_size = self.f.tell()
        self.f.seek(0,0)

    def one_page(self):
        for i in range(15):
            print self.f.readline(),
        self.current_size = self.f.tell()
        
    def percent(self):
        print '%.3f%%'%((self.current_size / float(self.total_size)) * 100)

    def __del__(self):
        self.f.close()

if __name__ == '__main__':
    a = OurReader('1.txt')   
    while True:
        contral = raw_input('Please enter:')
        if contral == 'manual':
            a.one_page()
            a.percent()
        elif contral == 'auto':
            while True:
                a.one_page()
                a.percent()
                time.sleep(3)

        elif contral == 'exit':
            break
    del a
        
'''

#python�����ļ�
    #.ini  .py  .conf  �ı��ļ�

import ConfigParser
con = ConfigParser.ConfigParser()
#print dir(con)
con.read('conf.ini')
#print con.sections()  ���������ļ����½���
#print con.options('CONF') ����ָ���½��µ�ѡ����

#print con.get('CONF','color') ��ȡָ���½���ѡ������Ӧ��ֵ
#print con.items('CONF') #��ָ���½��µ�ѡ���ֵ�ϲ���һ��Ԫ�鵱�У������б���ʽ

con.remove_section('DEMO') #ɾ��ָ�����½�
#print con.sections()
con.remove_option('CONF','name')  #ɾ��ָ���½��µ�ѡ��
#print con.options('CONF')

#con.add_section('HELLO') #����µ��½�
#print con.sections()
con.set('HELLO','name','xiaoqiang') #��ָ�����½������ָ����ѡ��
#print con.items('HELLO')
con.set('CONF','maskcolor','skyblue')
#print con.items('CONF')
#con.write(open('1.ini','w'))
#con.write(open('conf.ini','w'))

#print con.has_section('HELLO') 
#print con.has_section('AAA')
#print con.has_option('HELLO','name')
#print con.has_option('CONF','name')

    #�����ļ��ĸ�ʽ
'''
[�½���]
ѡ���� = ֵ or ѡ����:ֵ
'''
#SQLAlchemy



