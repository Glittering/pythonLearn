#coding:gbk


#python 是一门弱变量语言，变量的类型由值的类型决定，变量即用即生成

#python 列表
    #list()
    #[]
    #range()
    #列表的方法
        #列表的添加
            #append 在指定列表的末尾追加一个元素
'''
l = range(10)
l.append(100)
l.append('abc')
#print l
'''
            #extend 将可迭代对象拆分，依次添加到指定列表当中
'''
l = range(10)
l.append('abc')
l.extend('abc')
l.extend(['1','2','3'])
print l
'''
            #insert 在指定的索引位之前插入指定的元素
'''
l = range(10)
#print l
l.insert(3,'name')
print l
l.insert(6,'age')
print l
'''
        #列表的查找
            #count 在指定的列表当中，查找指定元素出现的次数
l = [1,25,2,65,2,44,25,15,25,2,25]
#print l.count(20)
            #index 在指定的列表当中查找指定的元素，如果存在，返回第一次出现的索引位
                   #如果不存在，报错
#print l.index(25)
#print l.index(25,3,7)

        #列表的删除
            #remove 在指定的列表当中，删除指定的元素
l = ['a',1,'b','a',2,'c',3]
#print l.remove('a')
#print l
            #pop 默认弹出最后一个索引位上的元素
#print l.pop()
'''
print l.pop(3)  #弹出指定索引位上的元素
print l
'''

        #列表的排序
            #sort  正排序
l = ['a','*',14,'R',35,'w','@',25,',','c','%','F','C']
#l.sort()
#print l
            #reverse 按索引倒排序
#l.reverse()
#print l
'''
l.sort()
l.reverse()
'''
'''
l.sort(reverse = True)
print l
'''


#sorted
#print sorted(l)
#print l

#reversed
'''
i = reversed(l)
print dir(i)
print i.next()
'''
#set
l = [1,25,2,65,2,44,25,15,25,2,25]
a = [1,3,5,7,9]
b = [2,4,1,3,6,8]

#print set(l)
#print set(a)|set(b)
#print set(a)&set(b)

#公共的方法
    #del
'''
del l[3]
print l
'''
'''
del l
print l
'''
'''
s = 'hello world'
#del s[4]
del s
print s
'''

#python 元组  因为元组的不可修改性，一般用元组写配置文件
    #定义
        #()
        #tuple()
        #单元素元组必须以逗号结尾
'''
>>> a = ([1,2,3])
>>> a
[1, 2, 3]
>>> (1)
1
>>> ('name')
'name'
>>> (1,)
(1,)
>>> ('name',)
('name',)
>>> ([1,2,3],)
([1, 2, 3],)
'''
t = tuple(range(2,10))
'''
print t[6]
print t[2:6]
print t[::-1]
print t[::2]
'''

    #元组的方法
        #count 在指定的元组当中，查找指定元素出现的次数
t = (2,3,'a','b','c','d','a',1,'2','a')
#print t.count('a')
        #index 在指定的元组当中查找指定元素，如果存在，返回第一次出现的索引位
               #如果不存在，报错
'''
print t.index('a',3,7)
print t.index('o')
'''


#python 字典：唯一一种映射关系的数据类型
    #字典的定义
        #{}
        #dict()
'''
>>> dict([['a',1]])
{'a': 1}
>>> dict([['a',1],['age',30]])
{'a': 1, 'age': 30}
>>> dict([('a',1),('age',30)])
{'a': 1, 'age': 30}

>>> dict((('name','xiaozhang'),))
{'name': 'xiaozhang'}
>>> dict((('name','xiaozhang'),(10,10)))
{10: 10, 'name': 'xiaozhang'}

>>> dict((['name','xiaozhang'],[10,10]))
{10: 10, 'name': 'xiaozhang'}
'''
        #dict(zip())
            #zip 将序列相同索引位上的元素合并到一个元组当中，并返回列表形式,以短序列为主

'''
>>> zip('abcd')
[('a',), ('b',), ('c',), ('d',)]
>>> zip('abcdefg',range(10))
[('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6)]
>>> zip('abcdefg',range(5),('A','B','C'))
[('a', 0, 'A'), ('b', 1, 'B'), ('c', 2, 'C')]
'''

'''
>>> dict(zip('abcd',range(5)))
{'a': 0, 'c': 2, 'b': 1, 'd': 3}
'''
    #字典的访问
        #以键取值
d = {'name':'laoli','age':30,'gender':'nan'}
#print d
#print d['name']
#print d['gender']
#print d['address']
#d['name'] = 'xiaoqiang'
#d['address'] = 'BeiJing'
#print d
'''
del d['gender']
print d
'''
    #字典的方法
        #get  在指定的字典当中获取指定键所对应的值，如果键存在，返回键所对应的值
              #如果键不存在，返回设置的默认值，没有默认值，返回None

#print d.get('age')
#print d.get('aaa')
#print d.get('aaa','hello world')
#print d.get('name','xiaoqiang')
#print d

        #setdefault 设置默认值，如果键存在返回键所对应的值。
                    #如果键不存在，向字典中添加一个元素
'''
#print d.setdefault('name')
print d.setdefault('aaa')
print d.setdefault('address','HaiNan')
print d
'''
d = {'name':'laoli','age':30,'gender':'nan'}

        #keys 获取指定字典的键
#print d.keys()
        #values 获取指定字典的值
#print d.values()
        #items 将字典的键和值合并到一个元组当中，并返回列表形式
#print d.items()

        #pop 弹出指定的键值对
'''
print d.pop('age')
print d.pop('aaa','hello')
#print d.pop('aaa')
print d
'''
        #popitem 随机弹出键值对
'''
print d.popitem()
print d
'''

        #update 更新
'''
d.update(name = 'xiaoqiang')
d.update(address = 'BeiJing',age = 20)
print d
'''
        #has_key 判断指定键是否在指定字典当中存在（python3不存在）
        #in
d = dict(zip('abcd',range(5)))
'''
print d.has_key('c')
print d.has_key('a')     
print d.has_key('f')
'''
#print 'a' in d
#print 'q' in d


        #视图模式
            #viewkeys
#print d.viewkeys()
            #viewvalus
#print d.viewvalues()
            #viewitems
#print d.viewitems()

        #迭代模式
            #iterkeys
#print d.iterkeys()
            #itervalues
#print d.itervalues()
            #iteritems
#print d.iteritems()

a = d.iteritems()
#print a.next()
'''
for i in d.iteritems():
    print i

print '\n'
for j in d.items():
    print j
'''
'''
for i in d.keys():
    print i

for i in d.iterkeys():
    print i
'''
        #clear 清空字典,保留字典队象
'''
d = dict(zip('abc',[1,2,3]))
print d
d.clear()
print d

del d
print d
'''
        #copy 拷贝一个对象
d = {'name':'xiaoqiang','age':20}
a = d.copy()
b = d
d['gender'] = 'nan'
#print a
#print d
'''
print b
print d
'''
import copy
    #copy.copy() 浅层拷贝，仅拷贝对象本身
    #copy.deepcopy() 深层拷贝

'''
zgyh = {'name':'','money':{'RMB':'','Dollar':''}}
laoli = zgyh.copy()
laoli['name'] = 'laoli'
laoli['money']['RMB'] = 5000
zgyh['money']['Dollar'] = 50

lisao = laoli.copy()
lisao['money']['RMB'] = 1000
lisao['name'] = 'lisao' 

print zgyh
print laoli
print lisao
'''


#python语句
    #print语句
        #2版本 语句
        #3版本 函数
        #将多个print语句打印在同一行，在语句末尾加 ,
'''
print 'hello world,',
print 'my name is xiaoqiang,',
print 'my job is ITmonkey!!!' 
'''
        #将多个内容打印在同一行，要用逗号隔开
'''
print 'hello world,''my name is xiaoqiang,''my job is ITmonkey!!!'  
print 'sad',[123]
'''
'''
print('hello world'),
print('hi'),
print('你好')
'''
    #import语句

import keyword
'''
#print keyword.kwlist
print keyword.iskeyword('for')
print keyword.iskeyword('abc')
'''
        #import 模块名
        #import 模块名 as 别名
#import DocXMLRPCServer
#import DocXMLRPCServer as a

        #from 模块名 import 方法名1,方法名2,...
        #from 模块名 import 方法名 as 别名

from keyword import kwlist
#print kwlist
'''
import time
print time.localtime()
'''
'''
from time import localtime,ctime
print localtime()
print ctime()
'''
#from time import *
'''
from time import localtime as abc

print abc()
'''

    #赋值语句
        #直接赋值语句
name = 'xiaoqiang'
age = 30 

        #链式赋值语句
x = y = z = 100

        #序列解包赋值
'''
x,y,z = '123'
print x,y,z
'''
#x,y,z = (10,20,30)
#x,y,z = ['abc',123,'age']

    #exec 执行字符串里面的python语句
'''
exec("print 'hello world'")
exec('print 100 * 5')
exec('import random')
'''
    #eval 执行字符串里的算术表达式

#print eval('100 * 100')
#print eval('100 / 20 + 100')
#print eval("print 'hello'")


#python 环境变量的配置
    #import sys  sys.path.append()  临时性的
    #我的电脑 --> 右击 --> 属性 --> 高级系统设置 --> 环境变量

#import demo
import sys
'''
print sys.path 
import hello
'''

    #顺序执行语句
    #条件执行语句
    #循环执行语句

#条件执行语句
    #if 条件表达式:
        #block语句块
'''
a = 100
a = -1
if a:
    print a
    print a * 10
'''

#True：非空字符串、非空列表、非空元祖、非空字典、非0数字

#Flase:空字符串、空列表、空元祖、空字典、0

'''
a = [1]
if a:
    print 'hello world'
'''

a = 100
'''
if a > 150:
    print 'the number may be so bigger.'
else:
    print 'hello'
'''
'''
if a > 0 and a <= 50:
    print a * 5
elif a > 50 and a < 100:
    print a + 100
else:
    print a
'''
'''
if a >= 0 and a <= 30:
    print a * 5
elif a > 30 and a <= 60:
    print a - 50
elif a > 60 and a <= 90:
    print a + 100
elif a > 90 and a <= 100:
    print a / 5
else:
    print a
'''

#获取键盘的输入（python3 input --> 字符串）
    #input 获取键盘输入的原类型
'''
>>> input('>>>')
>>>[123]
[123]
>>> input('>>>')
>>>{}
{}
>>> input('>>>')
>>>'aaa'
'aaa'
'''
    #raw_input 将输入的内容转换为字符串并获取
'''
>>> raw_input('>>>')
>>>100
'100'
>>> raw_input('>>>')
>>>[123]
'[123]'
>>> raw_input('>>>')
>>>(1,2,3)
'(1,2,3)'
'''


#循环执行语句
    #for循环(有循环次数的限制)
        #for var in 可迭代对象:
            #block语句块
'''
for i in range(10):
    print i
'''
'''
for i in 'abc':
    print i
'''
'''
for i in ' ':
    print i
'''
'''
for i in (1,2,3):
    print i
'''
'''
for i in {'name':'laoli','age':35}:
    print i
'''
'''
for i,j in {'name':'laoli','age':35}.items():
    print i,j
'''
#+=  -=  *=  /=
'''
a = 100
b = 50
#a = a + b
a += b
b -= a  #--> b = b - a
print a
print b
'''
'''
s = 0
for i in range(1,101):
    s += i
print s
'''
#sum(range(1,101))
'''
l1 = []
l2 = []
for i in range(15):
    if i % 2 == 0:
        l1.append(i)
    else:
        l2.append(i)

print l1
print l2
'''
'''
for i in range(5):
    for j in range(10):
        print i + j,
    print '\n'
'''

    #while循环（死循环）
        #while 条件表达式:
            #block
'''
while 1:
    print 'hello world'
'''
'''
while 0:
    print 'hello world'
'''
'''
a = 5
while a:
    print a * 10
    a -= 1
'''
'''
import random
guess_list = ['石头','剪刀','布']
a = 5
while a:
    print random.choice(guess_list)
    a -= 1
'''
'''
b = input('>>>')
#print b
'''

#break 终止当前循环
'''
while True:
    print 'hello world'
    break
'''
'''
while True:
    for i in range(10):
        print i
    break
'''
'''
for i in range(10):
    print i
    break
'''
#continue 终止本次循环，回到循环开始位置继续执行
'''
a = 5
while a:
    print a
    a -= 1
    continue
    print 'hello world'
'''

#pass 占位
'''
while True:
    pass
'''
'''
for i in range(10):
    pass
'''

'''
a = 10
if a > 5:
    pass
'''
'''
for _ in range(10):
    for j in range(5):
        print j + 3
'''

#用*来打印一个直角三角形
#用*打印一个空心正方形
#用*打印一个等腰梯形
#九九乘法表
#石头剪刀布
