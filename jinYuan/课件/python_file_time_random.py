#coding:gbk

'''
import wx
class MyEditor():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "Simple Editor",size = (410,335))
        self.panel = wx.Panel(self.frame)

        self.bt1 = wx.Button(self.panel,label = "open")
        self.bt1.Bind(wx.EVT_BUTTON,self.op)
        self.bt2 = wx.Button(self.panel,label = "save")
        self.bt2.Bind(wx.EVT_BUTTON,self.sa)

        self.filename = wx.TextCtrl(self.panel)
        self.content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)

        self.s_box = wx.BoxSizer()
        self.s_box.Add(self.filename,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box.Add(self.bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box.Add(self.bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

        self.panel.SetSizer(self.v_box)


    def op(self,event):
        path = self.filename.GetValue()
        f = open(path,'r')
        self.content.SetValue(f.read())
        f.close()

    def sa(self,event):
        path = self.filename.GetValue()
        f = open(path,'a')
        f.write(self.content.GetValue())
        #self.content.SetValue('')
        #self.content.write('123')
        #self.content.AppendText('name')
        f.close()

if __name__ == '__main__':
    a = MyEditor()
    a.frame.Show()
    a.app.MainLoop()
'''

'''
f = open('1.doc','r')
#print f.read(30)
print f.readlines()
f.close()
'''
'''
f = open('1.txt','r')
#f.seek(100,0)
f.seek(0,2)
#print f.read(10)
#f.seek(0,0)
print f.tell()
f.close()
'''
'''
f = open('python_django.py','r')
#f.seek(0,2)
#print f.tell()
#print len(f.read())
f.close()
'''
'''
f = open('1.txt','a')
f.seek(100,2)
#f.write('1234567890')
print f.tell()
f.close()
'''

#python ʱ��
import time
    #����ʱ
    #1970.01.01.0.0.0 ������ļ�Ԫʱ��
    #ʱ���  
    #UTCʱ�� 
    #˲��

#print time.localtime()  #���ر��ص�struct_time��ʽʱ��
#print time.time() #���ص�ǰʱ���ʱ���ʱ��

#print time.localtime(time.time())
#print time.localtime(3000000000)
'''
#print time.localtime()[-2]
print time.localtime().tm_yday
'''
#print time.localtime()
#print time.gmtime() #����UTCʱ����struct_time��ʽʱ��

#print time.mktime((1997,7,1,0,0,0,0,0,0))  #��struct_time��ʽʱ��ת��Ϊʱ���ʱ��
#print time.mktime((2016,12,12,12,12,12,0,0,0))

#print time.asctime() #��struct_timeʱ��ת��Ϊasctime��ʽʱ��

#print time.asctime((2016,11,11,11,11,11,0,0,0))

#print time.ctime(time.time()) ��ʱ���ʱ��ת��Ϊasctime��ʽʱ��
#print time.ctime(3000000000)

#print time.sleep(3000000) #���ߣ��������ʱ��
'''
time.sleep(5)
print 'hello world'
'''
'''
for i in range(5):
    time.sleep(i)
    print i
'''

#��Windows�У�time.clock(),��һ�ε��÷��س�������ʱ�䣬
            #�ٴε��õ�ʱ�򣬷��ؾ����һ�ε��ù�ȥ�೤ʱ��
'''
if __name__ == '__main__':
    print 'clock1:',time.clock()
    time.sleep(2)
    print 'clock2:',time.clock()
    time.sleep(3)
    print 'clock3:',time.clock()
'''
#time.strftime() ��struct_time��ʽʱ�䣬���ո�ʽ���ַ������
'''
print time.strftime('%Y,%m,%d')
print time.strftime('%y,%m,%d')
'''
#print time.strftime('%H:%M:%S')
#print time.strftime('%I:%M:%S')

#print time.strftime('%Y-%m-%d %H:%M:%S')
#print time.strftime('%I:%M:%S %p')

#print time.strftime('%a %b')
#print time.strftime('%A %B')

#print time.strftime('%c %Z')

#print time.strftime('%y')

#print time.strftime('%Y-%m-%d %I:%M:%S',(2017,3,30,13,12,30,0,0,0))


#python �����
import random

l = range(10)
for i in range(15):
    #print random.random()  #�������0-1֮��ĸ�����
    #print random.randint(10,20) #�������ָ����Χ֮���������������������
    #print random.randrange(10,20) #�������ָ����Χ֮����������������ޣ�������
    #print random.uniform(10,20) #�������ָ����Χ֮��ĸ�����
    #print random.uniform(10.5,20.5)
    #print random.randrange(10,20,2)
    #print random.sample(l,4) #��ָ�������е��������ȡָ��������Ԫ��
    #print random.sample('abcdefg',3)
    #print random.choice(l)  #��ָ�������е��������ȡһ��Ԫ��
    pass

#d = dict(zip('abcd',range(5)))
'''
for i in range(5):
    random.shuffle(l)
    print l
'''
'''
f = open('1.xls','w')
for i in range(1,10):
    for j in range(1,i + 1):
        f.write('%s*%s = %s\t'%(j,i,i * j))
    f.write('\n')
f.close()
'''

#���������λ��֤��
'''
code_list = []
for i in range(65,91):
    code_list.append(chr(i))

for j in range(97,123):
    code_list.append(chr(j))

for x in range(10):
    code_list.append(str(x))

#random.shuffle(code_list)

print ''.join(random.sample(code_list,6))
'''
'''
code = []
for i in range(6):
    if i == random.randint(0,2):
        code.append(str(random.choice(range(10))))
    elif i == random.randint(3,4):
        code.append(chr(random.randint(97,122)))
    else:
        code.append(chr(random.randint(65,90)))

print ''.join(code)
'''     


