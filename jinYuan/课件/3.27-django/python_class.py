#coding:gbk

#��������ħ������
    #__init__  ���캯������ʵ����֮���Զ�ִ��
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

    #__del__  ������������ɾ��ʵ��֮���Զ�ִ��
'''
class Demo():
    def __del__(self):
        print 'Bye-Bye'

d = Demo()
#d.__del__()
del d
'''
    #__name__ ����ָ���������ֵ��ַ�������
'''
class Demo():
    pass

print Demo.__name__
'''

    #__dict__ �����������������ֵ����ֵ�

class Demo():
    'abcdefg'
    name = 'xiaoli'
    def func(self):
        return 'welcome to my house'

#print Demo.__dict__

    #__doc__  ˵���ĵ��ַ���
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


    #dir ������ָ���������������ɵ��б�
#print dir(Demo)

class Hello():
    def __init__(self):
        print 'hello world'
    
#h = Hello()
'''
if __name__ == '__main__': #��������룬������䲻ִ��
    h = Hello()
'''

    
class Hero():
    hp = 100
    mp = 100
    def jn(self):
        self.mp -= 20
        return self.mp
#print Hero.jn()

    #hasattr �ж�ָ�����Ƿ����ָ��������
'''
print hasattr(Hero,'hp')
print hasattr(Hero,'aaa')
print hasattr(Hero,'jn')
'''
    #getattr ��ָ���൱�л�ȡָ�����Զ�Ӧ��ֵ

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

    #issubclass �ж�ָ�������Ƿ���ָ���������
class A():
    pass

class B(A):
    pass

#print issubclass(B,A)
 
    #isinstance �ж�ָ�������Ƿ���ָ�����ʵ��
b = B()

#print isinstance(b,B)
