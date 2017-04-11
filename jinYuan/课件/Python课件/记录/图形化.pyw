#coding:gbk
import wx

'''
app = wx.App() #实例化一个应用程序（主循环）
frame = wx.Frame(None) #实例化一个窗口组件
frame.Show()   #调用窗口组件的显示功能
app.MainLoop() #启动主循环
'''
'''
app = wx.App() 
frame = wx.Frame(None)

frame.Show() 
app.MainLoop()
'''


#Frame 窗口
    #parent 父组件，当为None时代表该组件为顶级组件
    #id     编号，对组件的标识，同一图形化界面当中不能出现id相同的情况，
            #当id为-1时，代表程序自动分配id
    #title  标题，窗口的标题
    #pos    组件的位置，需要一个双元素元组，形成坐标系，来规定组件距左和距上的距离
    #size   组件的大小，需要一个双元素元组，来规定组件的宽和高
    #style  组件的样式
    #name   名字，对组件的标识

#Button 按钮
    #label  按钮上的内容

#TextCtrl 文本输入框
    #value  文本输入框里面的内容

'''
app = wx.App()
frame = wx.Frame(None,title = "hello",size = (410,335))

bt1 = wx.Button(frame,label = "open",pos = (225,5),size = (80,25))
#bt2 = wx.Button(frame,label = "save",pos = (315,5),size = (80,25))

#filename = wx.TextCtrl(frame,pos = (5,5),size = (210,25))
#content = wx.TextCtrl(frame,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE|wx.HSCROLL)

frame.Show()
app.MainLoop()
'''

#尺寸器布局
    #Panel 画布，窗口的容器
    #1、创建尺寸器
        #BoxSizer
            #默认为水平尺寸器
            #垂直尺寸器
                #wx.VERTICAL
    #2、添加组件
        #Add
            #proportion 比例
            #flag
                #填充的样式
                    #wx.EXPAND 
                #填充的方向  --> 边框
                    #wx.TOP
                    #wx.BOTTOM
                    #wx.LEFT
                    #wx.RIGHT
                    #wx.ALL

            #border 边框

    #3、声明主尺寸器
        #SetSizer
'''

app = wx.App()
frame = wx.Frame(None,title = "hello",size = (410,335))
panel = wx.Panel(frame)

bt1 = wx.Button(panel,label = "open")
bt2 = wx.Button(panel,label = "save")

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.HSCROLL)

h_box = wx.BoxSizer()
h_box.Add(filename,proportion = 8,flag = wx.EXPAND|wx.LEFT,border = 1)
h_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
h_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)

frame.Show()
app.MainLoop()  

'''

#绑定事件
    #event
    #Bind
        #wx.EVT_BUTTON 按钮事件的总称
    #GetValue 获取值
    #SetValue 设置值

def dk(event):
    path = filename.GetValue()
    f = open(path,'r')
    content.SetValue(f.read())
    f.close()


app = wx.App()
frame = wx.Frame(None,title = "hello",size = (410,335))
panel = wx.Panel(frame)

bt1 = wx.Button(panel,label = "open")
bt1.Bind(wx.EVT_BUTTON,dk)
bt2 = wx.Button(panel,label = "save")

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel,style = wx.TE_MULTILINE)
 
h_box = wx.BoxSizer()
h_box.Add(filename,proportion = 8,flag = wx.EXPAND|wx.LEFT,border = 1)
h_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
h_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)

frame.Show()
app.MainLoop()  


