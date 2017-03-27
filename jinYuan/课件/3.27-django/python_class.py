#coding:gbk

#面向对象的魔术方法
    #__init__  构造函数，当实例化之后，自动执行
'''
class Demo():
    def __init__(self):
        print 'hello world'

d = Demo()
#d.__init__()
'''
'''
class Demo():
    def __init__(self,x,y):
        print x * y

d = Demo(100,20)
'''

    #__del__  析构函数，当删除实例之后，自动执行
'''
class Demo():
    def __del__(self):
        print 'Bye-Bye'

d = Demo()
#d.__del__()
del d
'''
    #__name__ 返回指定对象名字的字符串表现
'''
class Demo():
    pass

print Demo.__name__
'''

    #__dict__ 返回由类的属性名和值组成字典

class Demo():
    'abcdefg'
    name = 'xiaoli'
    def func(self):
        return 'welcome to my house'

#print Demo.__dict__

    #__doc__  说明文档字符串
'''
class Demo():
    
    #'abcdefg
    #hijklmn'
    name = 'xiaoli'
    def func(self):
        return 'welcome to my house'

print Demo.__doc__
'''
'''
    #__module__
class Demo():
    pass

print Demo.__module__
'''


    #dir 返回由指定对象的属性名组成的列表
#print dir(Demo)

class Hello():
    def __init__(self):
        print 'hello world'
    
#h = Hello()
'''
if __name__ == '__main__': #如果被导入，下面语句不执行
    h = Hello()
'''

    
class Hero():
    hp = 100
    mp = 100
    def jn(self):
        self.mp -= 20
        return self.mp
#print Hero.jn()

    #hasattr 判断指定类是否存在指定的属性
'''
print hasattr(Hero,'hp')
print hasattr(Hero,'aaa')
print hasattr(Hero,'jn')
'''
    #getattr 在指定类当中获取指定属性对应的值

#print getattr(Hero,'hp')

h = Hero()
#h.jn()  --> Hero.jn(h)

#print getattr(h,'jn')()
#print getattr(Hero,'jn')(h)

#print getattr(Hero,'aaa','unkown')

    #setattr 
setattr(Hero,'name','xiaoqiang')
#print dir(Hero)
#print Hero.__dict__
'''
def hello(self):
    print 'hello python'

setattr(Hero,'hi',hello)

h = Hero()
getattr(Hero,'hi')(h)
'''
    #delattr
delattr(Hero,'hp')
#print dir(Hero)
delattr(Hero,'jn')
#print dir(Hero)

    #issubclass 判断指定对象是否是指定类的子类
class A():
    pass

class B(A):
    pass

#print issubclass(B,A)
 
    #isinstance 判断指定对象是否是指定类的实例
b = B()

#print isinstance(b,B)
