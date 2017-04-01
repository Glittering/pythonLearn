#!/usr/bin/python2.7
#coding:gbk

import wx

'''
app = wx.App()   #ʵ����һ��Ӧ�ó�����ѭ����
frame = wx.Frame(None)  #ʵ����һ��ͼ�λ�����
frame.Show()     #����ͼ�λ����ڵ���ʾ����
app.MainLoop()   #������ѭ��
'''
'''
app = wx.App()   
frame = wx.Frame(None)

frame.Show()  
app.MainLoop()
'''

#Frame �������
    #parent ���������ΪNone��ʱ�򣬸����Ϊ�������
    #id ��ţ�������ı�ʶ����ͬһͼ�λ����浱�У����ܳ���id��ͬ�������
        #��idΪ-1ʱ������ϵͳ�Զ�����id
    #title ���⣬���ڵı���
    #pos   �����λ�ã���Ҫһ��˫Ԫ��Ԫ�飬���涨�������;��ϵľ���
    #size  ����Ĵ�С����Ҫһ��˫Ԫ��Ԫ�飬���涨����ĳ��͸�
    #style ��ʽ���������ʽ
    #name  ��������֣�������ı�ʶ

#Button ��ť
    #label ��ť�ϵ�����

#TextCtrl �ı������
    #value �ı�������������
'''
app = wx.App()
frame = wx.Frame(None,title = "Simple Editor",size = (410,335))

bt1 = wx.Button(frame,label = "open",pos = (225,5),size = (80,25))
bt2 = wx.Button(frame,label = "save",pos = (315,5),size = (80,25))

filename = wx.TextCtrl(frame,pos = (5,5),size = (210,25))
content = wx.TextCtrl(frame,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE|wx.HSCROLL)

frame.Show()
app.MainLoop()
'''


#�ߴ�������
    #Panel ���������ڵ���������ͼ�λ�����Ĵ�С��һ��
    #1�������ߴ���
        #wx.BoxSizer
            #Ĭ��Ϊˮƽ�ߴ���
            #wx.VERTICAL

    #2��������
        #Add
            #proportion ����
            #flag
                #������ʽ
                    #wx.EXPAND

                #���ķ���  --> border
                    #wx.ALL
                    #wx.TOP
                    #wx.BOTTOM
                    #wx.LEFT
                    #wx.RIGHT

            #border �߿�

    #3���������ߴ���
        #SetSizer


'''
app = wx.App()
frame = wx.Frame(None,title = "Simple Editor",size = (410,335))
panel = wx.Panel(frame)

bt1 = wx.Button(panel,label = "open")
bt2 = wx.Button(panel,label = "save")

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.HSCROLL)

s_box = wx.BoxSizer()
s_box.Add(filename,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)

frame.Show()
app.MainLoop()
'''

#���¼�
    #event
    #GetValue ��ȡֵ
    #Setvalue ����ֵ
    #write
    #AppendText

    #Bind
        #��ť EVT_BUTTON
'''
def op(event):
    path = filename.GetValue()
    f = open(path,'r')
    content.SetValue(f.read())
    f.close()


app = wx.App()
frame = wx.Frame(None,title = "Simple Editor",size = (410,335))
panel = wx.Panel(frame)

bt1 = wx.Button(panel,label = "open")
bt1.Bind(wx.EVT_BUTTON,op)
bt2 = wx.Button(panel,label = "save")

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel,style = wx.TE_MULTILINE)

s_box = wx.BoxSizer()
s_box.Add(filename,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)

frame.Show()
app.MainLoop()
'''

class MyEditor():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "Simple Editor",size = (410,335))
        self.panel = wx.Panel(self.frame)

        self.bt1 = wx.Button(self.panel,label = "open")
        self.bt1.Bind(wx.EVT_BUTTON,self.op)
        self.bt2 = wx.Button(self.panel,label = "save")

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

if __name__ == '__main__':
    a = MyEditor()
    a.frame.Show()
    a.app.MainLoop()






#python �ļ�����
    #.xls  xlwt  xlrd
    #.pdf  reportlab 
    #.tar  tarfile
    #.zip  zipfile
    #ͼƬ   pillow  pil

#1�������ļ���������
    #open
    #file
        #name --> path �ļ�·��
        #mode Ȩ��
            #r ��
            #w ����д
            #a ׷��д
            #rb �����ƵĶ�
            #wb �����Ƶ�д
            #rU ͨ�û��з��Ķ�
            #Ua ͨ�û��з���д
            #r+ w+ a+ ��д˫ģʽ

'''
f = file('python_django.py','r')
o = open('python_django.py','r')

print dir(f)
print '\n'
print dir(o)
'''

#2�����в���
    #��
        #read  ��ȫ��
        #readline ��һ��
        #readlines ���ж�ȫ�ģ������б���ʽ

    #д
        #write  д�ַ���
        #writelines д����

    #ָ��
        #seek
            #��һ��������ָ���ƶ�����Ծ���
            #�ڶ�������
                #0 �ӿ�ͷ
                #1 �ӵ�ǰ
                #2 ��ĩβ


        #tell ����ָ���λ��

#3���رղ�������
    #close

'''
f = open('python_django.py','r')
#print f.read(101)
#print f.readline(100)
print f.readlines()
f.close()
'''
'''
f = open('1.txt','r')
print f.readlines()
f.close()
'''
'''
f = open('1.txt','w')
f.write('abc')
f.close()
'''
'''
f = open('1.txt','a')
f.write('123')
f.close()
'''
'''
f = open('1.txt','a')
#f.writelines(['1','2','3'])
f.writelines('name')
f.close()
''' 
