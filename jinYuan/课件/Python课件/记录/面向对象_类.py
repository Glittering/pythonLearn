#coding:gbk

#��������Զ���һ�д��ڵĶ��Ƕ���

    #�ࣺ������Ļ���

        #�����������ʵ���ı���
            #�������������ı���
            #ʵ������������ʵ���ı���
        #������������ĺ���
        #���ԣ���ͷ�����ͳ��

    #ʵ������ľ��󻯣����������


        #��Ķ���
            #class ����(����): --> �շ�Ƿ�
                #block����
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
        #���ʵ����
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
    first_name = '����'
    last_name = '��'

class Child(Parent):
    pass
'''

#��ʵ�������ı�ʱ����������䣬����ʵ����������
#��������ı�ʱ��ʵ�������ı�

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
    #�������ķ������б�����һ������self�Ĳ����������ǽ���ʵ����ʵ��=����(),
    #���÷�����ʵ��.������()����ʱ��ϵͳ���Զ�ת��Ϊ����.����(ʵ��)��Ҳ����˵��
    #self����ʵ������
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

    #����������������
        #�̳�
'''
class Parent():
    first_name = '����'
    last_name = '��'

class Child(Parent):
    first_name = 'Ծ��'

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

#�����ࣺ���̳�object����,������࣬���;�������
#��ʽ�ࣺ�̳�object����,ģ�����������֮��Ľ���
'''
class Old():
    pass

class New(object):
    pass

print type(Old)
print type(New)
'''
#������ļ̳У����ռ̳�˳��̳�
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
#��ʽ��ļ̳У������޸����ȼ�
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

        #��װ
            #__var  __fname  ˽�л�����
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
        #��̬
'''
print 100 + 200
print 'abc' + '123'
print [1,2,3] + ['a','b','c']
'''

    #��������ħ������
        #__init__ ���캯������ʵ����֮���Զ�ִ��
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

        #__del__ ��������,ɾ��ʵ��֮���Զ�ִ��

'''
class Hello():
    def __del__(self):
        print '���'

h = Hello()
#h.__del__()
del h
'''

        #__doc__ ˵���ĵ��ַ���
'''
class Demo():
    'My name is xiaoli.'
    a = 100
    def hello(self):
        print '���'

        
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
        print '���'
    #'My name is xiaozhang.'

print Demo.__doc__
'''

        #__dict__ ����һ�����������������ɵ��ֵ�

class Demo():
    'My name is xiaoli.'
    a = 100
    def hello(self):
        print '���'

#print Demo.__dict__

        #__module__
#print Demo.__module__

        #__name__ ����ָ���������ֵ��ַ�������
#print Demo.__name__

'''
>>> def hello():
	pass

>>> hello.__name__
'hello'
'''

        #dir ����һ������������ɵ��б�
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


