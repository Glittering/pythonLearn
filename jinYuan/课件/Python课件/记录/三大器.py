#coding:gbk

#������
    #�������Ƿ��ʼ�����Ԫ�ص�һ�ַ�ʽ������������Ӽ��ϵĵ�һ��Ԫ�ؿ�ʼ���ʣ�
    #ֱ�����е�Ԫ�ض�������һ�����������������ܻ��ˣ�ֻ����ǰ���е�����
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


#������
    #��������������һ�ֵ�����,������ӵ��next����������Ϊ���������ȫ��ͬ,
    #����ζ��������Ҳ��������Python��forѭ����.����,�����������������﷨֧��ʹ��
    #��дһ�����������Զ���һ������ĵ�����Ҫ�򵥲���,����������Ҳ����õ�������֮һ.
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

#쳲���������
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

#װ������һ�������������ģʽ����������������������ĳ�������Ϊ������в�����־�����ܲ��ԡ�
#������ȡ�
#װ�����ǽ����������ľ�����ƣ�����װ���������ǾͿ��Գ���������������뺯�����ܱ����޹ص�
#��ͬ���벢�������á�
#�����Ľ���װ���������þ���Ϊ�Ѿ����ڵĶ�����Ӷ���Ĺ��ܡ�


'''
def shout(word = "yes"):
    return word.capitalize() + "!!!"

#print shout()

func = shout  #����shout��Ϊһ�����󣬰�shout��ֵ��func
print func()

del shout
print func()  #�����ɾ���ɵ�����shout����Ȼ����ͨ��func�����ʸú���
'''

'''
def a():
    def b(word = "Yes"):
        return word.lower() + "..."
    print b()

a()
'''

#�����������������ǿ��Եó���������Ȼ��Ϊһ��������ˣ�
    #1. ����Ա�������������
    #2. ����Ա�����������һ��������
#��Ҳ����˵���������Է���һ������
#��Ȼ���Է���һ�����������ǿ��԰�����Ϊ�������ݸ�����



#�滻����(װ��)
    #װ�κ����Ĳ����Ǳ�װ�εĺ�������,����ԭ��������
    #װ�ε�ʵ�����: myfunc = deco(myfunc)
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

#ʹ���﷨��@��װ�κ���,�൱��"myfunc = deco(myfunc)"
#�������º���ֻ�ڵ�һ�α�����,��ԭ�����������һ��
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


#ʹ����Ƕ��װ������ȷ��ÿ���º����������ã���Ƕ��װ������
#�βκͷ���ֵ��ԭ������ͬ,װ�κ���������Ƕ��װ��������
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

#�Դ������ĺ�������װ��,��Ƕ��װ�������βκͷ���ֵ��ԭ������ͬ,
#װ�κ���������Ƕ��װ��������
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
#�Բ���������ȷ���ĺ�������װ��,������(*args, **kwargs),
#�Զ���Ӧ��κ���������

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


#��ʾ��4�Ļ�����,��װ����������,����һʾ�������������һ���װ.
#װ�κ�����ʵ����Ӧ��������Щ
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

