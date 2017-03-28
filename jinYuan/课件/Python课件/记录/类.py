#coding:gbk

#python 类

    #issubclass 判断指定对象是否是指定类的子类
'''
class A():
    pass

class B(A):
    pass

print issubclass(B,A)
'''

    #isinstance 判断指定对象是否是指定类的实例
'''
class Hero():
    pass

h = Hero()

print isinstance(h,Hero)
'''

    #hasattr 判断指定类是否存在指定的属性
class Hero():
    hp = 100
    mp = 100

    def jn(self):
        self.mp -= 20
        return self.mp

#print hasattr(Hero,'hp')
#print hasattr(Hero,'jn')
#print hasattr(Hero,'abc')

    #getattr 获取指定类属性所对应的值
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



#python 随机数模块

import random

s = 'abcdefghijklmn'
l = range(5)
for i in range(30):
    #print random.random()  #随机生成0-1之间的浮点数
    #print random.randint(10,20)  #随机生成指定范围之间整数，包含上下限
    #print random.uniform(10,20)  #随机生成指定范围之间的浮点数
    #print random.randrange(10,20) #随机生成指定范围之间的整数，包含下限，不包含上限
    #print random.randrange(10)
    #print random.randrange(10,20,2)
    #print random.choice(s) #在指定的序列当中随机抽取一个元素
    #pass
    random.shuffle(l) #将指定的序列随机打乱顺序
    #print l
    #print random.sample(s,2) #在指定的序列当中随机抽取指定个数的元素，返回列表形式
    #print random.sample(l,3)
    pass


#生成验证码

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



#python 时间模块

import time,datetime,calendar
    #1970.01.01.0.0.0 计算机纪元时间
    #时间戳   
    #UTC时区  0时区
    #夏令时
    #瞬秒

#print time.localtime() #返回一个九元素元组的struct_time格式时间
#print time.time() #返回当前时间的时间戳时间

#print time.localtime(1000000000)
#print time.localtime()[-2]
#print time.localtime().tm_yday
'''
print time.localtime()
print time.gmtime() #返回UTC时区的struct_time格式时间
'''

#print time.mktime((2016,9,9,12,12,12,0,0,0)) #将struct_time格式时间转换为时间戳时间

'''
print time.asctime() #返回asctime格式时间
print time.asctime(time.localtime())
'''
#print time.asctime((2015,5,5,12,12,12,0,0,0))

'''
print time.ctime()   #将时间戳时间转换为asctime格式时间
print time.ctime(time.time())
print time.ctime(1000000000)
'''

#print 'hello world'
#time.sleep(3)  #休眠，程序挂起时间
#print '你好'
'''
for i in range(5):
    time.sleep(i)
    print i * 100
'''
#在Windows中，time.clock指的是，第一调用返回程序运行时间，再次调用程序距离第一次调用经过多少时间
#在Linux中，返回程序运行时间
'''
if __name__ == '__main__':
    print 'clock1：',time.clock()
    time.sleep(2)
    print 'clock2:',time.clock()
    time.sleep(3)
    print 'clock3:',time.clock()
'''

#print time.strftime('%Y,%m,%d')
#print time.strftime('%y-%m-%d')
print time.strftime('%H:%M:%S')
print time.strftime('%I:%M:%S')
