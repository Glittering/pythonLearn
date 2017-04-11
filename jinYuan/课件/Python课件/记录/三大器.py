#coding:gbk

#迭代器
    #迭代器是访问集合内元素的一种方式。迭代器对象从集合的第一个元素开始访问，
    #直到所有的元素都被访问一遍后结束。迭代器不能回退，只能往前进行迭代。
'''
a = range(5)
b = iter(a)
'''

'''
print b
print b.next()
print next(b)
print next(b)
print next(b)
print next(b)
print next(b)
'''
'''
a = range(10)
c = iter(a)
try:
    while True:
        print c.next()
except StopIteration:
    pass
'''


#生成器
    #首先生成器就是一种迭代器,生成器拥有next方法并且行为与迭代器完全相同,
    #这意味着生成器也可以用于Python的for循环中.另外,对于生成器的特殊语法支持使得
    #编写一个生成器比自定义一个常规的迭代器要简单不少,所以生成器也是最常用到的特性之一.
'''
def func():
    yield 0
    yield 1
    yield 2
    yield 3

    
#print func
#print func()

generator = func()
print generator.next()
print generator.next()
print generator.next()
print generator.next()
print generator.next()
'''

#斐波那契数列
'''
def fibo():
    a = b = 1
    yield a
    yield b
    while True:
        a,b = b,a+b
        yield b

for num in fibo():
    if num > 100:
        break
    #print num
    print num,

'''

#装饰器是一个很著名的设计模式，经常被用于有切面需求的场景，较为经典的有插入日志、性能测试、
#事务处理等。
#装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的
#雷同代码并继续重用。
#概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。


'''
def shout(word = "yes"):
    return word.capitalize() + "!!!"

#print shout()

func = shout  #函数shout作为一个对象，把shout赋值给func
print func()

del shout
print func()  #你可以删除旧的名字shout，仍然可以通过func来访问该函数
'''

'''
def a():
    def b(word = "Yes"):
        return word.lower() + "..."
    print b()

a()
'''

#从以上两个例子我们可以得出，函数既然作为一个对象，因此：
    #1. 其可以被赋给其他变量
    #2. 其可以被定义在另外一个函数内
#这也就是说，函数可以返回一个函数
#既然可以返回一个函数，我们可以把它作为参数传递给函数



#替换函数(装饰)
    #装饰函数的参数是被装饰的函数对象,返回原函数对象
    #装饰的实质语句: myfunc = deco(myfunc)
'''
def demo(func):
    print "before myfunc() called."
    func()
    print "after myfunc() called."
    return myfunc

def myfunc():
    print "myfunc() called."

myfunc = demo(myfunc)

myfunc()
'''

#使用语法糖@来装饰函数,相当于"myfunc = deco(myfunc)"
#但发现新函数只在第一次被调用,且原函数多调用了一次
'''
def demo(func):
    print("before myfunc() called.")
    func()
    print(" after myfunc() called.")
    return func
@demo
def myfunc():
    print(" myfunc() called.")
myfunc()
'''


#使用内嵌包装函数来确保每次新函数都被调用，内嵌包装函数的
#形参和返回值与原函数相同,装饰函数返回内嵌包装函数对象
'''
def demo(func):
    def _demo():
        print("before myfunc() called.")
        func()
        print(" after myfunc() called.")
    return _demo


@demo
def myfunc():
    print(" myfunc() called.")
myfunc()

#myfunc = demo(myfunc)
'''

#对带参数的函数进行装饰,内嵌包装函数的形参和返回值与原函数相同,
#装饰函数返回内嵌包装函数对象
'''
def demo(func):
    def _demo(a,b):
        print("before myfunc() called.")
        ret = func(a,b)
        print(" after myfunc() called. result: %s" % ret)
        return ret
    return _demo
@demo
def myfunc(a,b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a + b
myfunc(1, 2)
#myfunc(3, 4)
#myfunc = demo(myfunc)
'''
#对参数数量不确定的函数进行装饰,参数用(*args, **kwargs),
#自动适应变参和命名参数

def demo(func):
    def _demo(*args, **kwargs):
        print("before %s called." % func.__name__)
        ret = func(*args, **kwargs)
        print(" after %s called. result: %s" % (func.__name__, ret))
        return ret
    return _demo
@demo
def myfunc(a, b):
    print(" myfunc(%s,%s) called." % (a, b))
    return a+b
@demo
def myfunc2(a, b, c):
    print(" myfunc2(%s,%s,%s) called." % (a, b, c))
    return a+b+c

myfunc(1, 2)
#myfunc(3, 4)
myfunc2(1, 2, 3)
#myfunc2(3, 4, 5)


#在示例4的基础上,让装饰器带参数,和上一示例相比在外层多了一层包装.
#装饰函数名实际上应更有意义些
'''
def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print(" after %s called [%s]." % (func.__name__, arg))
        return __deco
    return _deco

@deco("module1")
def myfunc():
    print(" myfunc() called.")
    
@deco("module2")
def myfunc2():
    print(" myfunc2() called.")
    
myfunc()
myfunc2()
'''

#print 'asda','hello world','hello python'

'''
def outer(cs):
    cs()
    print 'hello world'
    #return cs   
@outer 
def inner():
    print 'hello python'
'''

'''
def a():
    print 'hello'

b = a
b()
b = a()
b
'''
'''
for i in range(10):
    print i

for _ in range(10):
    print 'hello world'

'''

'''
def demo1(func):
    func()
    print 'hello world'


def demo2():
    print 'HELLO PYTHON'

demo = demo1(demo2)

'''
'''
def demo1(func):
    func()
    print 'hello world'

@demo1  #--> demo = demo1(demo2)

def demo2():
    print 'HELLO PYTHON'
'''

