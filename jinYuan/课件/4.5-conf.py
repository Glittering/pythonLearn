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

#python配置文件
    #.ini  .py  .conf  文本文件

import ConfigParser
con = ConfigParser.ConfigParser()
#print dir(con)
con.read('conf.ini')
#print con.sections()  返回配置文件的章节名
#print con.options('CONF') 返回指定章节下的选项名

#print con.get('CONF','color') 获取指定章节下选项所对应的值
#print con.items('CONF') #将指定章节下的选项和值合并到一个元组当中，返回列表形式

con.remove_section('DEMO') #删除指定的章节
#print con.sections()
con.remove_option('CONF','name')  #删除指定章节下的选项
#print con.options('CONF')

#con.add_section('HELLO') #添加新的章节
#print con.sections()
con.set('HELLO','name','xiaoqiang') #在指定的章节下添加指定的选项
#print con.items('HELLO')
con.set('CONF','maskcolor','skyblue')
#print con.items('CONF')
#con.write(open('1.ini','w'))
#con.write(open('conf.ini','w'))

#print con.has_section('HELLO') 
#print con.has_section('AAA')
#print con.has_option('HELLO','name')
#print con.has_option('CONF','name')

    #配置文件的格式
'''
[章节名]
选项名 = 值 or 选项名:值
'''
#SQLAlchemy



