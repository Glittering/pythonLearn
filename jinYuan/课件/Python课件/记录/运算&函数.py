#coding:gbk

#python �Ƚ������
    #> < >= <= ==(ֵ���) != <> is(ȫ��)

#python �߼������
    #�� or  ����Ϊ��ȡǰ�ߣ�����Ϊ��
    #�� and ����Ϊ��ȡ���ߣ��м�Ϊ��
    #�� not
    #���ȼ� not > and > or 

'''
>>> 100 and 50
50
>>> 50 and 100
100
>>> 50 and 0
0
>>> 0 and 50
0
>>> 100 or 50
100
>>> 50 or 100
50
>>> 50 or 0
50
>>> 0 or 50
50
'''

'''
>>> not c and b
False
>>> True or True and False
True
>>> False and True or True
True
>>> not True and False
False
>>> not True or True
True
'''


#python ��������
    #True:�ǿ��ַ������ǿ��б��ǿ��ֵ䡢�ǿ�Ԫ�桢��0����
    #False:���ַ��������б����ֵ䡢��Ԫ�桢0

'''
l = [1,2,3]
print help(l.sort)
'''

#cmp �Ƚ�ֵ��С
    #��x > yʱ������1
    #��x < yʱ������-1
    #��x = yʱ������0
'''
print cmp(20,10)
print cmp(10,20)
print cmp(10,10)
'''

#repr ���ַ���ͬʱת��Ϊ�ַ�����һ����
'''
print repr(100)
>>> repr('hello')
"'hello'"
>>> str('hello')
'hello'
'''

#enumerate ö��,���ͳ����ļ���

'''
>>> l = range(2,11)
>>> l
[2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a = enumerate(l)
>>> a
<enumerate object at 0x00000000024FDEA0>

>>> for i in a:
	print i

	
(5, 7)
(6, 8)
(7, 9)
(8, 10)
'''

#python ���ָ���
    # \ 
    # ( )
    # ''' '''   """ """

'''
>>> a = 10
>>> if a >\
   5:
	print 'hello'

	
hello
'''
#>>> if a > 5:
#	print '''hello,
#I'am ITmonket!!!
#'''

	
#hello,
#I'am ITmonket!!!

'''
>>> if a > 5:
	print ('hello:',
	       'laoli')

	
('hello:', 'laoli')
'''
'''
>>> if (a >
    5):
	print 'hello'

	
hello
'''


#python �������ǶԳ����߼����нṹ������̻���һ�ֱ�̷�����
    #�����Ķ���
        #def fname([arg1[,arg2][,...]):
            #block����

        #lambda һ�к���
            #lambda arg1[,arg2][,...]:�������ʽ

def hello():
    print 'hello python'

    #�����ĵ���
        #fname([arg1[,arg2][,...])

#hello()

'''
def demo():
    a = 100
    b = 50
    a += b
    print a

demo()
'''

def func(arg):
    print arg * 10

#func([123])
#func()
#print func
'''
s = lambda x,y:x*y
print s(100,30)
'''
d = {'a':1,'aa':15,'aaaa':10,'aaa':5}
#print d
l = d.items()
print l
print l.sort()
print l.sort(key = lambda x:x[-1])

def value(x):
    return x[-1]  

l.sort(key = value)

#print l

#print value(['a','abc','age','123']) #--> print '123'


#map

#print map(None,'abc',range(5))
#��������ͬ����λ�ϵ�Ԫ�غϲ���һ��Ԫ�鵱�У������б���ʽ���Գ���Ϊ�����������None����

#print zip('abc',range(5))
#��������ͬ����λ�ϵ�Ԫ�غϲ���һ��Ԫ�鵱�У������б���ʽ���Զ̵�Ϊ��


#print map(lambda x,y:x * y,'abcdefg',range(1,8))

#쳲���������
'''
def fb(num):
    fibo = [1,2]
    for i in range(num - 2):
        fibo.append(fibo[-1] + fibo[-2])
    print fibo

fb(10)
'''
#���
'''
def qh(num):
    a = 0
    for i in range(1,num + 1):
        a += i
    print a
          
qh(200)
'''

    #�����Ĳ���
        #�βΣ������Ƕ��庯��ʱ������Ĳ���
        #ʵ�Σ������ǵ��ú����ǣ����ݵĲ���

        #λ�ò���:�����ǵ��ú���������ʵ�ε�ʱ�򣬰������Ƕ����βε�˳�����
'''
def demo(x,y,z):
    print 'x is:',x
    print 'y is:',y
    print 'z is:',z
    print x + y + z

demo(50,10,20)
'''
        #�ؼ��ֲ���:�����ǵ��ú���������ʵ�ε�ʱ�򣬰����β�=ʵ�ν��У��Ӷ����Ժ��Դ��ε�˳��
'''
def demo(x,y,z):
    print 'x is:',x
    print 'y is:',y
    print 'z is:',z
    print x + y + z

demo(x = 20,z = 50,y = 10)
'''
def demo(x,y,z):
    print x
    print y
    print z
    
#demo(10,20,z = 50)

#demo(x = 10,y = 20,50)

        #Ĭ�ϲ���:�����Ƕ��庯����ʱ�򣬸��βδ���Ĭ��ֵ�������ǵ��ú���������ʵ�ε�ʱ�����ǿ��Ժ��Դ���Ĭ��ֵ�Ĳ���
'''
def demo(x,y,z = 100):
    print x
    print y
    print z

#demo(10,50)
#demo(10,50,20)
demo(z = 30,y = 50,x = 100)
'''
        #������
            #����ǰ��һ��*,�γ�Ԫ���Ͳ���
            #����ǰ������*,�γ��ֵ��Ͳ���
'''
def func(*arg):
    print arg

func('hello',100,[123])
'''
'''
def func(**arg):
    print arg

func(name = 'xiaoqiang')
'''
'''
def func(*arg,**kwarg):
    print arg
    print kwarg.items()
    

func(100,name = 'xiaoqiang')
'''

    #return ����һ�������return������䲻��ִ��
'''
def demo(a,b):
    for i in range(a):
        pass
    return i * b
print demo(10,'a')
'''
'''
def demo(a,b):
    return a * b
    print 'hello world'
print demo(10,'a')
'''

    #callable �ж�ָ�������ܷ񱻵���
'''
def hello():
    print 'hello world'

a = [1,2,3]
print callable(hello)
print callable(a)
'''


#�б��ȥ��
'''
l = [2,'a',34,5,'b','a',123,'c','a']
r = []
for i in l:
    if i not in r:
        r.append(i)

print r
'''
'''
def qc(l):
    result = []
    for i in l:
        if i not in result:
            result.append(i)
    return result

print qc([1,3,5,2,3,5,2,6,10])
'''
#�б�Ľ���
'''
def jj(a,b):
    result = []
    for i in a:
        for j in b:
            if i == j:
                result.append(i)
    return result

print jj(range(5),[10,2,15,3,25,1])
'''
#�б�Ĳ���
'''
def bj(a,b):
    result = []
    for i in a:
        for j in b:
            if i == j:
                result.append(i)
            elif i != j:
                result.append(j)
    return result

print bj(range(5),[10,2,15,3,25,1])
'''
'''
a = [1,3,5,7,9]
b = [2,4,5,6,8,9]

c = a + b
r = []
for i in c:
    if i not in r:
        r.append(i)

print r
'''
'''
a = [1,3,5,7,9]
b = [2,4,5,6,8,9]
result = []
for i in a:
    if i not in result:
        result.append(i)

for j in b:
    if j not in result:
        result.append(j)

print result
'''
