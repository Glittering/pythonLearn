#coding:gbk
import wx

def op1(event):  
    finename.write('1')
def op2(event):  
    finename.write('2')
def op3(event):  
    finename.write('3')
def op4(event):  
    finename.write('+')
def op5(event):  
    finename.write('4')
def op6(event):  
    finename.write('5')
def op7(event):  
    finename.write('6')
def op8(event):  
    finename.write('-')
def op9(event):  
    finename.write('7')
def op10(event):  
    finename.write('8')
def op11(event):  
    finename.write('9')
def op12(event):  
    finename.write('*')
def op13(event):  
    finename.write('.')
def op14(event):  
    finename.write('0')
def op16(event):  
    finename.write('/')
def jieguo(event):
    result = eval(finename.GetValue())
    finename.SetValue(str(result))
def d(event):
    finename.Clear()
    finename.write('0')
def c(event):
    zhi = finename.GetValue()
    finename.SetValue(zhi[:-1])
app = wx.App()
win = wx.Frame(None,title = "simple Editor",size = (430,375))
panel = wx.Panel(win)
bt1 = wx.Button(panel,label = "1")
bt1.Bind(wx.EVT_BUTTON,op1)
bt2 = wx.Button(panel,label = "2")
bt2.Bind(wx.EVT_BUTTON,op2)
bt3 = wx.Button(panel,label = "3")
bt3.Bind(wx.EVT_BUTTON,op3)
bt4 = wx.Button(panel,label = "+")
bt4.Bind(wx.EVT_BUTTON,op4)
bt5 = wx.Button(panel,label = "4")
bt5.Bind(wx.EVT_BUTTON,op5)
bt6 = wx.Button(panel,label = "5")
bt6.Bind(wx.EVT_BUTTON,op6)
bt7 = wx.Button(panel,label = "6")
bt7.Bind(wx.EVT_BUTTON,op7)
bt8 = wx.Button(panel,label = "-")
bt8.Bind(wx.EVT_BUTTON,op8)
bt9 = wx.Button(panel,label = "7")
bt9.Bind(wx.EVT_BUTTON,op9)
bt10 = wx.Button(panel,label = "8")
bt10.Bind(wx.EVT_BUTTON,op10)
bt11 = wx.Button(panel,label = "9")
bt11.Bind(wx.EVT_BUTTON,op11)
bt12 = wx.Button(panel,label = "*")
bt12.Bind(wx.EVT_BUTTON,op12)
bt13 = wx.Button(panel,label = ".")
bt13.Bind(wx.EVT_BUTTON,op13)
bt14 = wx.Button(panel,label = "0")
bt14.Bind(wx.EVT_BUTTON,op14)
bt15 = wx.Button(panel,label = "=")
bt15.Bind(wx.EVT_BUTTON,jieguo)
bt16 = wx.Button(panel,label = "/")
bt16.Bind(wx.EVT_BUTTON,op16)
bt17 = wx.Button(panel,label = "c")
bt17.Bind(wx.EVT_BUTTON,d)
bt18 = wx.Button(panel,label = "del")
bt18.Bind(wx.EVT_BUTTON,c)
finename = wx.TextCtrl(panel)

s1_box = wx.BoxSizer(wx.VERTICAL)
s1_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s1_box.Add(bt5,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s1_box.Add(bt9,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s1_box.Add(bt13,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

s2_box = wx.BoxSizer(wx.VERTICAL)
s2_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s2_box.Add(bt6,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s2_box.Add(bt10,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s2_box.Add(bt14,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

s3_box = wx.BoxSizer(wx.VERTICAL)
s3_box.Add(bt3,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s3_box.Add(bt7,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s3_box.Add(bt11,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s3_box.Add(bt15,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

s4_box = wx.BoxSizer(wx.VERTICAL)
s4_box.Add(bt4,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s4_box.Add(bt8,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s4_box.Add(bt12,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s4_box.Add(bt16,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v1_box = wx.BoxSizer(wx.VERTICAL)
v1_box.Add(bt17,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v1_box.Add(bt18,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer()
v_box.Add(s1_box,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(s2_box,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(s3_box,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(s4_box,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(v1_box,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 1)

s_box = wx.BoxSizer(wx.VERTICAL)
s_box.Add(finename,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
s_box.Add(v_box,proportion = 10,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(s_box)
win.Show()
app.MainLoop()

