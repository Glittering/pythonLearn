#!D:\Python27\python.exe 
#coding:gbk
#! usr/bin/env python


#我的电脑 --> 右击 --> 属性 --> 高级系统设置 --> 环境变量

#print 100 * 100
#print(100*100)
#注释
    #单行注释 #
    #多行注释 
        #三单引号 ''' '''
        #三双引号 """ """

#.py 脚本文件
#.pyc 临时文件
#.pyw 图形化文件

#内置模块 Lib
#三方模块 Lib\site-packages
    #压缩包，解压，在CMD中切换目录，切到解压目录之下找到setup.py，然后执行python setup.py install
    #.exe 

#自写模块 
#import hello
import time

#dir() 查看指定对象的属性
#help() 查看属性的具体用法



#python 数字运算
    #整形数 int
    #长整形数 long
    #浮点数 float
    #数字运算符
        #+ - * / % **  //地板除

#len查看指定对象的长度

#python 数据类型
    #int
    #long
    #float
    #字符串 str:以引号包围的，元素可以是任意类型的,有序的、不可修改的序列
        #字符串的定义
            #str
            #''
            #" "
            #''' '''   """ """  支持换行
        #特殊字符
            #\n 换行符
            #\t 水平制表符
            #\v 垂直制表符
        #占位符
            #%s 
            #%d 传递整形数
            #%f 传递浮点数 '%0.3f'
'''
>>> 'a%10sb'%'hello'
'a     hellob'
>>> '%10d'%123
'       123'
>>> '%-10d'%123
'123       '
'''


        #字符串的格式化
            # % 格式化符
            #format
'''
>>> 'name:%s,age:%d'%('xiaoli',20)
'name:xiaoli,age:20'

>>> 'name:{0},age:{1}'.format('xiaoli',20)
'name:xiaoli,age:20'
>>> 'name:{1},age:{0}'.format('xiaoli',20)
'name:20,age:xiaoli'
'''

#name = 'laoli'  将等于号右边的值赋值给左边的变量

'''
>>> name = 'laozhang'
>>> age = 30
>>> 'name:{0},age:{1}'.format(name,age)
'name:laozhang,age:30'
>>> 'name:%s,age:%d'%(name,age)
'name:laozhang,age:30'
'''
        #转义符
            #\
            #% 只转义自身

'''
>>> '%d%'%10

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    '%d%'%10
ValueError: incomplete format
>>> '%d%%'%10
'10%'
>>> '%d\%'%10

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    '%d\%'%10
ValueError: incomplete format
'''
        #字符串的分片操作(索引操作)
s = 'hello python'
#print s[0]
#print s[4]
#print s[10]
#print s[-2]
'''
print s[1:10]  #有下限，无上限
print s[4:9]
'''
#print s[4:]
#print s[:10]
#print s[1:10]
#print s[1:10:2]  #步长为2
#print s[1:10:3]
#print s
#print s[::]
#print s[::2]
#print s[::-1]
#print s[1:10:-1]
'''
print s[::-2]
print s[1:10:-2]
'''
        #字符串的变形 --> 字母

            #upper 将小写字母转换为大写字母
s = 'Hello World'
#print s.upper()
#print s
            #lower 将大写字母转换为小写字母
#print s.lower()

            #title 单词首字符大写
#print 'hi,I am xiaozhen'.title()

            #capitalize 字符串首字符大写
#print 'Hi,I am Xiaozhen'.capitalize()

            #swapcase 大小写互换
#print s.swapcase()

#print '[123abc,'.upper()

        #字符串的填充
            #center 在指定的字符长度上居中，不足的地方默认以空白符填充
'''
s = '12345'
print s.center(15)
'''
            #ljust  在指定的字符长度上左对齐
s = 'hello'
'''
print s.ljust(15)
print s.ljust(15,'*')
'''
            #rjust  在指定的字符长度上右对齐
#print s.rjust(15)
#print s.rjust(15,'0')

            #zfill 在指定的字符长度上右对齐，默认以0填充
#print s.zfill(15)

#range(10)
            #expandtabs
                #\t 默认为8个字符长度
'''
print 'a\tb'
print 'a\tb'.expandtabs(15)
'''
        #字符串的删减
            #strip  默认删除字符串两端的空白符
s = '   hello world       '
#print s
#print s.strip()
a = 'hellohh'
#print a.strip('h')
#print a

            #lstrip 默认删除字符串左边的空白符
#print s.lstrip()
#print a.lstrip('h')

            #rstrip 默认删除字符串右边的空白符
#print s.rstrip()



        #字符串的切分
            #split 默认以空白符从左到右切分指定的字符串
s = "My name is xiaoqiang,my job is ITmonkey!!!"
#print s.split()
#print s.split('o')
#print s.split('o',2) #用指定的字符以规定的次数切分字符串

            #rsplit 默认以空白符从右到左切分指定的字符串
#print s.rsplit('o',2)


        #字符串的拼接
            #join 将可迭代对象拆分，循环添加

a = 'hello'
b = 'abc'
#print a.join(b)

            # + 拼接
#print a + b

            # * 重复
#print 'abc' * 10
            

        #字符串的查找
            #find 在指定的字符串当中，从左到右查找指定的字符，如果存在，返回第一次出现的索引位
                  #如果不存在，返回-1
            #rfind
s = "My name is xiaoqiang,my job is ITmonkey!!!"
#print s.find('o')
#print s[14]
#print s.find('o',15)
'''
print s.find('o',15,25)
print s.find('o',14,26)
'''
#print s.rfind('o')

            #index 在指定的字符串当中，从左到右查找指定的字符，如果存在，返回第一次出现的索引位
                   #如果不存在，报错
#print s.index('o')
#print s.index('o',15,25)

            #rindex

            #count 在指定的字符串当中查找指定字符出现的次数
#print s.count('o')
#print s.count('o',15)
#print s.count('o',15,25)
            
           

        #字符串的判断
            #isalnum 判断指定字符串是否完全由数字或字母组成
s = 'hello:123'
#print s.isalnum()
            #isalpha 判断指定字符串是否完全由字母组成
'''
print s.isalpha()
print 'ABCabc'.isalpha()
'''
            #isdigit 判断指定字符串是否完全由数字组成
#print '12345'.isdigit()

            #isspace 判断指定字符串是否完全由空白符组成
#print '123 abc'.isspace()
#print '   '.isspace()


            #isupper 判断指定字符串是否完全有大写字母组成
s = 'Hello wolrd'
#print s.isupper()
#print 'ABC'.isupper()

            #islower 判断指定字符串是否完全有小写字母组成
#print 'abc'.islower()

            #istitle 判断是否符合title
#print s.istitle()


            #startswith 判断指定字符串是否以指定字符开头
'''
#print 'My name is xiaoli.'.startswith('a')
print 'My name is xiaoli.'.startswith('My name')
'''
#print 'My name is xiaoli.'.startswith('a',4,10)

            #endswith  判断指定字符串是否以指定字符结尾
#print 'My name is xiaoli.'.endswith('li.')
#print 'My name is xiaoli.'.endswith('xiao',7,15)


        #字符串的编码
            #encode 加码
            #decode 解码
#print '中文'.encode('utf-8')
#print '中文'.decode('gbk')
#GB2312
#cp936
#unicode


        #字符串的替换
            #replace 将原有字符替换为指定的字符，可以规定替换的次数
s = 'hello world'
#print s.replace('l','*')
#print s.replace('ll','*',2)




    #列表 list:以中括号包围的，元素可以是任意类型的，元素之间以逗号隔开的，有序的、可修改的序列
        #列表的定义
            #list()
            #[]
            #range()

'''
>>> list('123')
['1', '2', '3']
>>> list((123,456,'abc'))
[123, 456, 'abc']
>>> [1,2,3]
[1, 2, 3]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(11)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1,11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1,11,2)
[1, 3, 5, 7, 9]
>>> range(1,11,3)
[1, 4, 7, 10]
'''
#xrange
'''
>>> l = range(10)
>>> type(l)
<type 'list'>
>>> a = xrange(10)
>>> type(a)
<type 'xrange'>
'''
        #列表的索引
l = range(1,11)
#print l[0]
#print l[1:5]
#print l[::2]
#print l[::-1]
l = ['name',['age',['gender',['address',100]]]]
#print len(l)
'''
a = l[1]
b = a[1]
c = b[1]
print c[1]
'''
#print l[1][1][1][-1]


    #元组 tuple:以小括号包围的，元素可以是任意类型的，元素之间以逗号隔开的，有序的、不可修改的序列
    #字典 dict：以大括号包围的，元素呈键值对显示的，元素之间以逗号隔开的，无序的、可修改的序列
    #字节 bytes

'''
以中括号包围的，
元素可以是任意类型的，
元素之间以逗号隔开的，
有序的、可修改的序列。
'''



