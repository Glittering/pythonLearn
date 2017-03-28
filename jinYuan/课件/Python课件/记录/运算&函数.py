#coding:gbk

#python 比较运算符
    #> < >= <= ==(值相等) != <> is(全等)

#python 逻辑运算符
    #或 or  两边为真取前者，有真为真
    #且 and 两边为真取后者，有假为假
    #非 not
    #优先级 not > and > or 

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


#python 布尔类型
    #True:非空字符串、非空列表、非空字典、非空元祖、非0数字
    #False:空字符串、空列表、空字典、空元祖、0

'''
l = [1,2,3]
print help(l.sort)
'''

#cmp 比较值大小
    #当x > y时，返回1
    #当x < y时，返回-1
    #当x = y时，返回0
'''
print cmp(20,10)
print cmp(10,20)
print cmp(10,10)
'''

#repr 把字符串同时转换为字符串的一部分
'''
print repr(100)
>>> repr('hello')
"'hello'"
>>> str('hello')
'hello'
'''

#enumerate 枚举,整型常数的集合

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

#python 语句分隔符
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


#python 函数：是对程序逻辑进行结构化或过程化的一种编程方法。
    #函数的定义
        #def fname([arg1[,arg2][,...]):
            #block语句块

        #lambda 一行函数
            #lambda arg1[,arg2][,...]:参数表达式

def hello():
    print 'hello python'

    #函数的调用
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
#将序列相同索引位上的元素合并到一个元组当中，返回列表形式，以长的为主，不足的以None补充

#print zip('abc',range(5))
#将序列相同索引位上的元素合并到一个元组当中，返回列表形式，以短的为主


#print map(lambda x,y:x * y,'abcdefg',range(1,8))

#斐波那契数列
'''
def fb(num):
    fibo = [1,2]
    for i in range(num - 2):
        fibo.append(fibo[-1] + fibo[-2])
    print fibo

fb(10)
'''
#求和
'''
def qh(num):
    a = 0
    for i in range(1,num + 1):
        a += i
    print a
          
qh(200)
'''

    #函数的参数
        #形参：当我们定义函数时，定义的参数
        #实参：当我们调用函数是，传递的参数

        #位置参数:当我们调用函数，传递实参的时候，按照我们定义形参的顺序进行
'''
def demo(x,y,z):
    print 'x is:',x
    print 'y is:',y
    print 'z is:',z
    print x + y + z

demo(50,10,20)
'''
        #关键字参数:当我们调用函数，传递实参的时候，按照形参=实参进行，从而可以忽略传参的顺序
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

        #默认参数:当我们定义函数的时候，给形参传递默认值，当我们调用函数，传递实参的时候，我们可以忽略传递默认值的参数
'''
def demo(x,y,z = 100):
    print x
    print y
    print z

#demo(10,50)
#demo(10,50,20)
demo(z = 30,y = 50,x = 100)
'''
        #参数组
            #参数前面一个*,形成元组型参数
            #参数前面两个*,形成字典型参数
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

    #return 返回一个结果，return下面语句不被执行
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

    #callable 判断指定对象能否被调用
'''
def hello():
    print 'hello world'

a = [1,2,3]
print callable(hello)
print callable(a)
'''


#列表的去重
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
#列表的交集
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
#列表的并集
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
