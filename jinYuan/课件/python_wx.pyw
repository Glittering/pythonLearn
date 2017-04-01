#!/usr/bin/python2.7
#coding:gbk

import wx

'''
app = wx.App()   #实例化一个应用程序（主循环）
frame = wx.Frame(None)  #实例化一个图形化窗口
frame.Show()     #调用图形化窗口的显示功能
app.MainLoop()   #启动主循环
'''
'''
app = wx.App()   
frame = wx.Frame(None)

frame.Show()  
app.MainLoop()
'''

#Frame 窗口组件
    #parent 父组件，当为None的时候，该组件为顶级组件
    #id 编号，对组件的标识，在同一图形化界面当中，不能出现id相同的组件，
        #当id为-1时，代表系统自动分配id
    #title 标题，窗口的标题
    #pos   组件的位置，需要一个双元素元组，来规定组件距左和距上的距离
    #size  组件的大小，需要一个双元素元组，来规定组件的长和高
    #style 样式，组件的样式
    #name  组件的名字，对组件的标识

#Button 按钮
    #label 按钮上的内容

#TextCtrl 文本输入框
    #value 文本输入框里的内容
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


#尺寸器布局
    #Panel 画布，窗口的容器，与图形化界面的大小相一致
    #1、创建尺寸器
        #wx.BoxSizer
            #默认为水平尺寸器
            #wx.VERTICAL

    #2、添加组件
        #Add
            #proportion 比例
            #flag
                #填充的样式
                    #wx.EXPAND

                #填充的方向  --> border
                    #wx.ALL
                    #wx.TOP
                    #wx.BOTTOM
                    #wx.LEFT
                    #wx.RIGHT

            #border 边框

    #3、声明主尺寸器
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

#绑定事件
    #event
    #GetValue 获取值
    #Setvalue 设置值
    #write
    #AppendText

    #Bind
        #按钮 EVT_BUTTON
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






#python 文件操作
    #.xls  xlwt  xlrd
    #.pdf  reportlab 
    #.tar  tarfile
    #.zip  zipfile
    #图片   pillow  pil

#1、创建文件操作队象
    #open
    #file
        #name --> path 文件路径
        #mode 权限
            #r 读
            #w 覆盖写
            #a 追加写
            #rb 二进制的读
            #wb 二进制的写
            #rU 通用换行符的读
            #Ua 通用换行符的写
            #r+ w+ a+ 读写双模式

'''
f = file('python_django.py','r')
o = open('python_django.py','r')

print dir(f)
print '\n'
print dir(o)
'''

#2、进行操作
    #读
        #read  读全文
        #readline 读一行
        #readlines 以行读全文，返回列表形式

    #写
        #write  写字符串
        #writelines 写序列

    #指针
        #seek
            #第一个参数：指针移动的相对距离
            #第二个参数
                #0 从开头
                #1 从当前
                #2 从末尾


        #tell 返回指针的位置

#3、关闭操作对象
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
