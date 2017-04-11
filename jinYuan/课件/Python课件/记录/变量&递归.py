#coding:gbk

#zip
'''
def compare(arg1,arg2):
    a = len(arg1)
    b = len(arg2)
    if a > b:
        return b
    else:
        return a

def myzip(arg1,arg2):
    result = []
    for i in range(compare(arg1,arg2)):
        result.append((arg1[i],arg2[i]))
    return result

print myzip(range(2,10),'asdfg')
'''

#python 作用域:函数或变量起作用的范围
    #L local 本地（局部）作用域
    #E 嵌套作用域
    #G global 全局作用域
    #B bulit-in 内建作用域


#局部变量
'''
def hello():
    x = 100
    y = 50
    x += y
    print x

hello()
print x * 10
'''

#全局变量
'''
x = 100
def hello():
    print x * 20

hello()
print x + 50 
'''
'''
x = 100
def hello(x):
    print 'x is:',x
    x = 20
    print 'x changed:',x

hello(x)
print 'x still is:',x
'''

#global 将局部变量声明为全局变量
'''
x = 100
def hello():
    print 'x is:',x
    global x
    x = 20
    print 'x changed:',x

hello()
print 'x still is:',x
'''

#嵌套作用域
'''
def hello(arg):
    #arg = str(arg)
    def hi():
        print 'hello:' + arg
    return hi

a = hello('xiaoqiang')
a()

hello('xiaoqiang')()
b = 100
c = '123'
'''
#闭包
'''
def outer(x):
    def inner(y):
        print x * y
    return inner

#outer('hello')(10)
a = outer
b = outer(10)
#print a
#print b
'''

#递归函数
    #递归：程序自身调用自身
    #条件
        #必须有一个出口（最小可能性）
        #程序自身应用自身

'''
def hello():
    print 'hello world'
    return hello()

hello()
'''

#阶乘
'''
def jc(num):
    a = 1
    for i in range(1,num + 1):
        a *= i
    print a

jc(5)
'''
'''
def demo(num):
    if num == 1:
        return 1
    else:
        return num * demo(num - 1)

print demo(10)
'''

'''
10 * demo(9)
10 * 9 * demo(8)
10 * 9 * 8 * demo(7)
10 * 9 * 8 * 7 * demo(6)
10 * 9 * 8 * 7 * 6 * demo(5)
.
.
.
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * demo(1)
10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
'''

#幂运算
'''
def demo(d,z):
    a = 1
    for i in range(z):
        a *= d
    return a
print demo(4,4)
'''
'''
def demo(d,z):
    if z == 0:
        return 1
    else:
        return d * demo(d,z - 1)

#print demo(4,4)
'''
'''
4 * demo(4,3)
4 * 4 * demo(4,2)
4 * 4 * 4 * demo(4,1)
4 * 4 * 4 * 4 * demo(4,0)
4 * 4 * 4 * 4 * 1
'''
#二元查找
l = [1,3,5,7,9,13,17,15,19,21,23,35,67,34]
a = 13

#os  sys

import os    
#print os.path


#小球落体
'''
def demo(num):
    if num / 2.0 < 1:
        return 1      
    else:
        return num + num/2.0 + demo(num/2.0)

print demo(100)
'''
'''
100 + 50 + demo(50)

100 + 50 + 50 + 25 + demo(25)

100 + 50 + 50 + 25 + 25 + 12.5 + demo(12.5)
'''
#sum dir help type len zip map sorted reversed vars cmp chr ord print
#repr str list tuple dict int float eval emumerate set range xrange iter next

#函数的三大器
    #迭代器
l = range(1,6)
i = iter(l)
#print dir(i)
#print i.next()
'''
for x in i:
    print x
'''
'''
print next(i)
print i.next()
'''
'''
for x in range(10):
    #print next(i)
    print i.next()
''' 
    #生成器:特殊的迭代器
'''
def hello():
    for i in 'abcdefg':
        yield i

a = hello()
#print dir(a)
print a.next()
print next(a)
'''
    #装饰器
