#coding:gbk

#python ��

    #issubclass �ж�ָ�������Ƿ���ָ���������
'''
class A():
    pass

class B(A):
    pass

print issubclass(B,A)
'''

    #isinstance �ж�ָ�������Ƿ���ָ�����ʵ��
'''
class Hero():
    pass

h = Hero()

print isinstance(h,Hero)
'''

    #hasattr �ж�ָ�����Ƿ����ָ��������
class Hero():
    hp = 100
    mp = 100

    def jn(self):
        self.mp -= 20
        return self.mp

#print hasattr(Hero,'hp')
#print hasattr(Hero,'jn')
#print hasattr(Hero,'abc')

    #getattr ��ȡָ������������Ӧ��ֵ
#print getattr(Hero,'hp')
#print getattr(Hero,'mp','hello world')
#print getattr(Hero,'abc','hello world')
'''
dema = Hero()
#print getattr(Hero,'jn')
print getattr(dema,'jn')()  #--> dema.jn()
print getattr(Hero,'jn')(dema)    #--> Hero.jn(dema)
'''

class Hero():
    hp = 100
    mp = 100

    def jn(self):
        self.mp -= 20
        return self.mp
    #setattr 
setattr(Hero,'name','xiaoli')
#print Hero.__dict__
#print getattr(Hero,'name')

def hello(self):
    print 'hello world'

setattr(Hero,'hello',hello)
#print Hero.__dict__
dema = Hero()
#getattr(Hero,'hello')(dema)

    #delattr
#delattr(Hero,'hp')
#print getattr(Hero,'hp')

delattr(Hero,'jn')
#print getattr(Hero,'jn')(dema)



#python �����ģ��

import random

s = 'abcdefghijklmn'
l = range(5)
for i in range(30):
    #print random.random()  #�������0-1֮��ĸ�����
    #print random.randint(10,20)  #�������ָ����Χ֮������������������
    #print random.uniform(10,20)  #�������ָ����Χ֮��ĸ�����
    #print random.randrange(10,20) #�������ָ����Χ֮����������������ޣ�����������
    #print random.randrange(10)
    #print random.randrange(10,20,2)
    #print random.choice(s) #��ָ�������е��������ȡһ��Ԫ��
    #pass
    random.shuffle(l) #��ָ���������������˳��
    #print l
    #print random.sample(s,2) #��ָ�������е��������ȡָ��������Ԫ�أ������б���ʽ
    #print random.sample(l,3)
    pass


#������֤��

code_list = []
digit = [str(x) for x in range(10)]
upper = [chr(i) for i in range(65,91)]
lower = [chr(j) for j in range(97,123)]

code_list = digit + upper + lower
#print code_list
random.shuffle(code_list)
#print code_list
#for i in range(10):
#print random.sample(code_list,6)
#print ''.join(random.sample(code_list,6))

#pillow pil

code = []
for i in range(6):
    if i == random.randrange(0,2):
        code.append(str(random.randint(0,9)))
    elif i == random.randrange(2,4):
        code.append(chr(random.randint(97,122)))
    else:
        code.append(chr(random.randint(65,90)))
random.shuffle(code)
#print ''.join(code)



#python ʱ��ģ��

import time,datetime,calendar
    #1970.01.01.0.0.0 �������Ԫʱ��
    #ʱ���   
    #UTCʱ��  0ʱ��
    #����ʱ
    #˲��

#print time.localtime() #����һ����Ԫ��Ԫ���struct_time��ʽʱ��
#print time.time() #���ص�ǰʱ���ʱ���ʱ��

#print time.localtime(1000000000)
#print time.localtime()[-2]
#print time.localtime().tm_yday
'''
print time.localtime()
print time.gmtime() #����UTCʱ����struct_time��ʽʱ��
'''

#print time.mktime((2016,9,9,12,12,12,0,0,0)) #��struct_time��ʽʱ��ת��Ϊʱ���ʱ��

'''
print time.asctime() #����asctime��ʽʱ��
print time.asctime(time.localtime())
'''
#print time.asctime((2015,5,5,12,12,12,0,0,0))

'''
print time.ctime()   #��ʱ���ʱ��ת��Ϊasctime��ʽʱ��
print time.ctime(time.time())
print time.ctime(1000000000)
'''

#print 'hello world'
#time.sleep(3)  #���ߣ��������ʱ��
#print '���'
'''
for i in range(5):
    time.sleep(i)
    print i * 100
'''
#��Windows�У�time.clockָ���ǣ���һ���÷��س�������ʱ�䣬�ٴε��ó�������һ�ε��þ�������ʱ��
#��Linux�У����س�������ʱ��
'''
if __name__ == '__main__':
    print 'clock1��',time.clock()
    time.sleep(2)
    print 'clock2:',time.clock()
    time.sleep(3)
    print 'clock3:',time.clock()
'''

#print time.strftime('%Y,%m,%d')
#print time.strftime('%y-%m-%d')
print time.strftime('%H:%M:%S')
print time.strftime('%I:%M:%S')
