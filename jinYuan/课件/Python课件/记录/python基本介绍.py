#coding:gbk


#python ��һ�����������ԣ�������������ֵ�����;������������ü�����

#python �б�
    #list()
    #[]
    #range()
    #�б�ķ���
        #�б�����
            #append ��ָ���б��ĩβ׷��һ��Ԫ��
'''
l = range(10)
l.append(100)
l.append('abc')
#print l
'''
            #extend ���ɵ��������֣�������ӵ�ָ���б���
'''
l = range(10)
l.append('abc')
l.extend('abc')
l.extend(['1','2','3'])
print l
'''
            #insert ��ָ��������λ֮ǰ����ָ����Ԫ��
'''
l = range(10)
#print l
l.insert(3,'name')
print l
l.insert(6,'age')
print l
'''
        #�б�Ĳ���
            #count ��ָ�����б��У�����ָ��Ԫ�س��ֵĴ���
l = [1,25,2,65,2,44,25,15,25,2,25]
#print l.count(20)
            #index ��ָ�����б��в���ָ����Ԫ�أ�������ڣ����ص�һ�γ��ֵ�����λ
                   #��������ڣ�����
#print l.index(25)
#print l.index(25,3,7)

        #�б��ɾ��
            #remove ��ָ�����б��У�ɾ��ָ����Ԫ��
l = ['a',1,'b','a',2,'c',3]
#print l.remove('a')
#print l
            #pop Ĭ�ϵ������һ������λ�ϵ�Ԫ��
#print l.pop()
'''
print l.pop(3)  #����ָ������λ�ϵ�Ԫ��
print l
'''

        #�б������
            #sort  ������
l = ['a','*',14,'R',35,'w','@',25,',','c','%','F','C']
#l.sort()
#print l
            #reverse ������������
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

#�����ķ���
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

#python Ԫ��  ��ΪԪ��Ĳ����޸��ԣ�һ����Ԫ��д�����ļ�
    #����
        #()
        #tuple()
        #��Ԫ��Ԫ������Զ��Ž�β
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

    #Ԫ��ķ���
        #count ��ָ����Ԫ�鵱�У�����ָ��Ԫ�س��ֵĴ���
t = (2,3,'a','b','c','d','a',1,'2','a')
#print t.count('a')
        #index ��ָ����Ԫ�鵱�в���ָ��Ԫ�أ�������ڣ����ص�һ�γ��ֵ�����λ
               #��������ڣ�����
'''
print t.index('a',3,7)
print t.index('o')
'''


#python �ֵ䣺Ψһһ��ӳ���ϵ����������
    #�ֵ�Ķ���
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
            #zip ��������ͬ����λ�ϵ�Ԫ�غϲ���һ��Ԫ�鵱�У��������б���ʽ,�Զ�����Ϊ��

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
    #�ֵ�ķ���
        #�Լ�ȡֵ
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
    #�ֵ�ķ���
        #get  ��ָ�����ֵ䵱�л�ȡָ��������Ӧ��ֵ����������ڣ����ؼ�����Ӧ��ֵ
              #����������ڣ��������õ�Ĭ��ֵ��û��Ĭ��ֵ������None

#print d.get('age')
#print d.get('aaa')
#print d.get('aaa','hello world')
#print d.get('name','xiaoqiang')
#print d

        #setdefault ����Ĭ��ֵ����������ڷ��ؼ�����Ӧ��ֵ��
                    #����������ڣ����ֵ������һ��Ԫ��
'''
#print d.setdefault('name')
print d.setdefault('aaa')
print d.setdefault('address','HaiNan')
print d
'''
d = {'name':'laoli','age':30,'gender':'nan'}

        #keys ��ȡָ���ֵ�ļ�
#print d.keys()
        #values ��ȡָ���ֵ��ֵ
#print d.values()
        #items ���ֵ�ļ���ֵ�ϲ���һ��Ԫ�鵱�У��������б���ʽ
#print d.items()

        #pop ����ָ���ļ�ֵ��
'''
print d.pop('age')
print d.pop('aaa','hello')
#print d.pop('aaa')
print d
'''
        #popitem ���������ֵ��
'''
print d.popitem()
print d
'''

        #update ����
'''
d.update(name = 'xiaoqiang')
d.update(address = 'BeiJing',age = 20)
print d
'''
        #has_key �ж�ָ�����Ƿ���ָ���ֵ䵱�д��ڣ�python3�����ڣ�
        #in
d = dict(zip('abcd',range(5)))
'''
print d.has_key('c')
print d.has_key('a')     
print d.has_key('f')
'''
#print 'a' in d
#print 'q' in d


        #��ͼģʽ
            #viewkeys
#print d.viewkeys()
            #viewvalus
#print d.viewvalues()
            #viewitems
#print d.viewitems()

        #����ģʽ
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
        #clear ����ֵ�,�����ֵ����
'''
d = dict(zip('abc',[1,2,3]))
print d
d.clear()
print d

del d
print d
'''
        #copy ����һ������
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
    #copy.copy() ǳ�㿽����������������
    #copy.deepcopy() ��㿽��

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


#python���
    #print���
        #2�汾 ���
        #3�汾 ����
        #�����print����ӡ��ͬһ�У������ĩβ�� ,
'''
print 'hello world,',
print 'my name is xiaoqiang,',
print 'my job is ITmonkey!!!' 
'''
        #��������ݴ�ӡ��ͬһ�У�Ҫ�ö��Ÿ���
'''
print 'hello world,''my name is xiaoqiang,''my job is ITmonkey!!!'  
print 'sad',[123]
'''
'''
print('hello world'),
print('hi'),
print('���')
'''
    #import���

import keyword
'''
#print keyword.kwlist
print keyword.iskeyword('for')
print keyword.iskeyword('abc')
'''
        #import ģ����
        #import ģ���� as ����
#import DocXMLRPCServer
#import DocXMLRPCServer as a

        #from ģ���� import ������1,������2,...
        #from ģ���� import ������ as ����

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

    #��ֵ���
        #ֱ�Ӹ�ֵ���
name = 'xiaoqiang'
age = 30 

        #��ʽ��ֵ���
x = y = z = 100

        #���н����ֵ
'''
x,y,z = '123'
print x,y,z
'''
#x,y,z = (10,20,30)
#x,y,z = ['abc',123,'age']

    #exec ִ���ַ��������python���
'''
exec("print 'hello world'")
exec('print 100 * 5')
exec('import random')
'''
    #eval ִ���ַ�������������ʽ

#print eval('100 * 100')
#print eval('100 / 20 + 100')
#print eval("print 'hello'")


#python ��������������
    #import sys  sys.path.append()  ��ʱ�Ե�
    #�ҵĵ��� --> �һ� --> ���� --> �߼�ϵͳ���� --> ��������

#import demo
import sys
'''
print sys.path 
import hello
'''

    #˳��ִ�����
    #����ִ�����
    #ѭ��ִ�����

#����ִ�����
    #if �������ʽ:
        #block����
'''
a = 100
a = -1
if a:
    print a
    print a * 10
'''

#True���ǿ��ַ������ǿ��б��ǿ�Ԫ�桢�ǿ��ֵ䡢��0����

#Flase:���ַ��������б���Ԫ�桢���ֵ䡢0

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

#��ȡ���̵����루python3 input --> �ַ�����
    #input ��ȡ���������ԭ����
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
    #raw_input �����������ת��Ϊ�ַ�������ȡ
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


#ѭ��ִ�����
    #forѭ��(��ѭ������������)
        #for var in �ɵ�������:
            #block����
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

    #whileѭ������ѭ����
        #while �������ʽ:
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
guess_list = ['ʯͷ','����','��']
a = 5
while a:
    print random.choice(guess_list)
    a -= 1
'''
'''
b = input('>>>')
#print b
'''

#break ��ֹ��ǰѭ��
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
#continue ��ֹ����ѭ�����ص�ѭ����ʼλ�ü���ִ��
'''
a = 5
while a:
    print a
    a -= 1
    continue
    print 'hello world'
'''

#pass ռλ
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

#��*����ӡһ��ֱ��������
#��*��ӡһ������������
#��*��ӡһ����������
#�žų˷���
#ʯͷ������
