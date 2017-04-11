#coding:gbk

#对象：万物皆对象，一切存在的都是对象

    #类：对事物的划分

        #域：属于类或者实例的变量
            #类变量：属于类的变量
            #实例变量：属于实例的变量
        #方法：属于类的函数
        #属性：域和方法的统称

    #实例：类的具象化，具体的事物


        #类的定义
            #class 类名(父类): --> 驼峰记法
                #block语句块
'''
class Hello():
    pass
#print type(Hello)

def hello():
    pass
'''
'''
class Person_Yellow_Chinese():
    pass
'''
        #类的实例化
'''
class Hero():
    hp = 100
    mp = 100

huangzi = Hero()
zhaoxin = Hero()
dema = Hero()
'''
'''
class Parent():
    first_name = '爱国'
    last_name = '郝'

class Child(Parent):
    pass
'''

#当实例变量改变时，类变量不变，其他实例变量不变
#当类变量改变时，实例变量改变

'''
class Hero():
    hp = 100
    mp = 100

dema = Hero()
dema.hp = 20
Hero.mp = 120
#print 'Hero.hp:',Hero.hp
print 'Hero.mp:',Hero.mp

#print 'dema.hp:',dema.hp
print 'dema.mp:',dema.mp

zhaoxin = Hero()

#print 'zhaoxin.hp:',zhaoxin.hp
print 'zhaoxin.mp:',zhaoxin.mp
'''
'''
class Hero():
    hp = 100
    mp = 100
    def jn(self):
        Hero.mp -= 20
        print Hero.mp

dema = Hero()
dema.jn()
'''
'''
class Hero():
    hp = 100
    mp = 100
    def jn1(self):
        if self.jn2():
            self.hp += 10
        return self.hp
    
    def jn2(self):
        return 1
    
huangzi = Hero()
print huangzi.jn1()
'''

#self
    #面向对象的方法当中必须有一个叫做self的参数，当我们进行实例化实例=类名(),
    #调用方法（实例.方法名()）的时候，系统会自动转换为：类.方法(实例)，也就是说，
    #self就是实例本身。
'''
class Hero():
    def hello(self):
        print self
        print '\n'
        
a = Hero()
print a
a.hello()


b = Hero()
print b
b.hello()
'''
'''
class Hero():
    hp = 100
    mp = 100
    def jn1(self):
        self.mp -= 20
        
    def jn2(self):
        self.mp += 10

a = Hero()
a.jn1()
'''

    #面向对象的三大特征
        #继承
'''
class Parent():
    first_name = '爱国'
    last_name = '郝'

class Child(Parent):
    first_name = '跃民'

tom = Child()

print tom.first_name
print tom.last_name
'''
'''
class A():
    a = 10
    b = 50
    def hello(self):
        print 'Hello world'

class B(A):
    def hello(self,arg):
        print arg * 5

c = B()
print c.a
c.hello('hi')
'''

#经典类：不继承object对象,类就是类，类型就是类型
#新式类：继承object对象,模糊了类和类型之间的界限
'''
class Old():
    pass

class New(object):
    pass

print type(Old)
print type(New)
'''
#经典类的继承：按照继承顺序继承
'''
class A():
    def hello(self):
        print 'I am A'

class B(A):
    pass

class C(A):
    def hello(self):
        print 'I am C'

class D(C,B):
    pass

d = D()
d.hello()
'''
#新式类的继承：按照修改优先级
'''
class A(object):
    def hello(self):
        print 'I am A'

class B(A):
    pass

class C(A):
    def hello(self):
        print 'I am C'

class D(C,B):
    pass

d = D()
d.hello()
'''
'''
class A():
    def hello(self):
        print 'I am A'

class B(A):
    def hello(self):
        print 'I am B'

class C(A):
    def hello(self):
        print 'I am C'

class D(B,C):
    pass

d = D()
d.hello()
'''
'''
class A(object):
    def hello(self):
        print 'I am A'

class B(A):
    def hello(self):
        print 'I am B'

class C(A):
    def hello(self):
        print 'I am C'

class D(B,C):
    pass

d = D()
d.hello()
'''

        #封装
            #__var  __fname  私有化属性
'''
class Hello():
    name = 'xiaozhang'
    __age = 20

h = Hello()
print h.name
print Hello.__age
print h.__age
'''
'''
class Hello():
    __name = 'xiaozhang'

    def demo(self):
        return self.__name

h = Hello()
#print h.__name
print h.demo()
'''
'''
class Hello():
    def __func(self):
        print 'hello world'

    def demo(self):
        return self.__func()

h = Hello()
#h.__func()
h.demo()
'''
        #多态
'''
print 100 + 200
print 'abc' + '123'
print [1,2,3] + ['a','b','c']
'''

    #面向对象的魔术方法
        #__init__ 构造函数，当实例化之后，自动执行
'''
class Hello():
    def __init__(self):
        print 'hello world'

h = Hello()
#h.__init__()
'''

class Hello():
    def __init__(self,name,age):
        print 'name:%s,age:%s'%(name,age)

#h = Hello('xiaoqiang',20)
#Hello('laoli',40)

        #__del__ 析构函数,删除实例之后，自动执行

'''
class Hello():
    def __del__(self):
        print '你好'

h = Hello()
#h.__del__()
del h
'''

        #__doc__ 说明文档字符串
'''
class Demo():
    'My name is xiaoli.'
    a = 100
    def hello(self):
        print '你好'

        
#print Demo.__doc__

def func():
    '1234567890'
    print 'hello'

print func.__doc__
'''
'''
class Demo():
    #a = 100
    'My name is xiaozhang.'
    def hello(self):
        print '你好'
    #'My name is xiaozhang.'

print Demo.__doc__
'''

        #__dict__ 返回一个由类的数据属性组成的字典

class Demo():
    'My name is xiaoli.'
    a = 100
    def hello(self):
        print '你好'

#print Demo.__dict__

        #__module__
#print Demo.__module__

        #__name__ 返回指定对象名字的字符串表现
#print Demo.__name__

'''
>>> def hello():
	pass

>>> hello.__name__
'hello'
'''

        #dir 返回一个由属性名组成的列表
#print dir(Demo)


class Hero():
    hp = 100
    mp = 100
    def jn(self):
        self.mp -= 20
        print self.mp

'''
if __name__ == '__main__':
    h = Hero()
    h.jn()
'''
#h = Hero()
#h.jn()


