#coding:gbk

import wx,thread,socket
'''
app=wx.App()    #实例化一个应用程序（实例化主循环）
frame=wx.Frame(None)    #实例化一个窗口组件
frame.Show()    #调用窗口组建的显示功能
app.MainLoop()  #启动主循环
'''
class user():
    def __init__(self):
        self.a=wx.App()
        self.f=wx.Frame(None,title='客户端',size=(600,600))
        self.p=wx.Panel(self.f)
        
        self.xx=wx.TextCtrl(self.p)
        self.xr=wx.TextCtrl(self.p)
        self.fs=wx.Button(self.p,label='发送')
        self.fs.Bind(wx.EVT_BUTTON,self.send)
        
        self.h=wx.BoxSizer()
        self.h1=wx.BoxSizer()
        self.s=wx.BoxSizer(wx.VERTICAL)
        
        self.h.Add(self.xx,proportion=5,flag=wx.EXPAND|wx.ALL,border=1)
        self.h1.Add(self.xr,proportion=4,flag=wx.EXPAND|wx.ALL,border=1)
        self.h1.Add(self.fs,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        
        self.s.Add(self.h,proportion=6,flag=wx.EXPAND|wx.ALL,border=1)
        self.s.Add(self.h1,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        
        self.p.SetSizer(self.s)
    def sock(self):
        self.khd=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.khd.connect(('127.0.0.1',9000))
        
        while True:
            self.recvs=self.khd.recv(512)
            self.xx.write(self.recvs)
    def send(self,event):
        self.sends=self.xr.GetValue()
        self.xx.write(self.sends)
        self.sock.send(self.sends)

    def duoxiancheng(self):
        thread.start_new_thread(self.sock,())
            


if __name__=='__main__':
    u=user()
    u.duoxiancheng()
    u.f.Show()
    u.a.MainLoop()

'''
def d1(event):
    a.AppendText('1')   
def d2(event):
    a.AppendText('2')
def d3(event):
    a.AppendText('3')
def d4(event):
    a.AppendText('4')
def d5(event):
    a.AppendText('5')
def d6(event):
    a.AppendText('6')
def d7(event):
    a.AppendText('7')
def d8(event):
    a.AppendText('8')
def d9(event):
    a.AppendText('9')
def d10(event):
    a.AppendText('0')
def d11(event):
    a.AppendText('+')
def d12(event):
    a.AppendText('-')
def d13(event):
    a.AppendText('*')
def d14(event):
    a.Clear()
def d15(event):
    a.AppendText('/')
def d16(event):
    E=a.GetValue()
    
    if E.find('+')!=-1:
        e=E.find('+')
        e1=''.join(E[:e])
        e2=''.join(E[e+1:])
        ee=float(e1)+float(e2)
    elif E.find('-')!=-1:
        e=E.find('-')
        e1=''.join(E[:e])
        e2=''.join(E[e+1:])
        ee=float(e1)-float(e2)
    elif E.find('*')!=-1:
        e=E.find('*')
        e1=''.join(E[:e])
        e2=''.join(E[e+1:])
        ee=float(e1)*float(e2)
    elif E.find('/')!=-1:
        e=E.find('/')
        e1=''.join(E[:e])
        e2=''.join(E[e+1:])
        ee=float(e1)/float(e2)
    ea=str(ee)
    if ea[-1] == '0':
        ea=ea[:-1]
    a.SetValue(ea)
    
def d17(event):
    a.AppendText('.')
def d18(event):
    A=a.GetValue()
    A=A[:-1]
    a.SetValue(A)
    
    
jisuanqi = wx.App()
frame = wx.Frame(None,title = "计算器初级版",size = (500,400))
p=wx.Panel(frame)
a = wx.TextCtrl(p)
a1 = wx.Button(p,label = "1")
a2 = wx.Button(p,label = "2")
a3 = wx.Button(p,label = "3")
a11 = wx.Button(p,label = "+")
a16 = wx.Button(p,label = "=")
a4 = wx.Button(p,label = "4")
a5 = wx.Button(p,label = "5")
a6 = wx.Button(p,label = "6")
a12 = wx.Button(p,label = "-")
a7 = wx.Button(p,label = "7")
a8 = wx.Button(p,label = "8")
a9 = wx.Button(p,label = "9")
a13 = wx.Button(p,label = "*")
a10 = wx.Button(p,label = "0")
a14 = wx.Button(p,label = "AC")
a15 = wx.Button(p,label = "/")
a17 = wx.Button(p,label = ".")
a18 = wx.Button(p,label = "<--")
h=wx.BoxSizer()
h1=wx.BoxSizer()
h2=wx.BoxSizer()
h3=wx.BoxSizer()
h4=wx.BoxSizer()

s=wx.BoxSizer(wx.VERTICAL)

h.Add(a,proportion=2,flag=wx.EXPAND|wx.ALL,border=1)
h.Add(a16,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h.Add(a18,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h1.Add(a1,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h1.Add(a2,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h1.Add(a3,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h1.Add(a11,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h2.Add(a4,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h2.Add(a5,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h2.Add(a6,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h2.Add(a12,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h3.Add(a7,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h3.Add(a8,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h3.Add(a9,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h3.Add(a13,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h4.Add(a17,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h4.Add(a10,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h4.Add(a14,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
h4.Add(a15,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

s.Add(h,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s.Add(h1,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s.Add(h2,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s.Add(h3,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
s.Add(h4,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)

#a.Bind(wx.EVT_BUTTON,d)
a1.Bind(wx.EVT_BUTTON,d1)
a2.Bind(wx.EVT_BUTTON,d2)
a3.Bind(wx.EVT_BUTTON,d3)
a11.Bind(wx.EVT_BUTTON,d11)
a16.Bind(wx.EVT_BUTTON,d16)
a4.Bind(wx.EVT_BUTTON,d4)
a5.Bind(wx.EVT_BUTTON,d5)
a6.Bind(wx.EVT_BUTTON,d6)
a12.Bind(wx.EVT_BUTTON,d12)
a7.Bind(wx.EVT_BUTTON,d7)
a8.Bind(wx.EVT_BUTTON,d8)
a9.Bind(wx.EVT_BUTTON,d9)
a13.Bind(wx.EVT_BUTTON,d13)
a10.Bind(wx.EVT_BUTTON,d10)
a14.Bind(wx.EVT_BUTTON,d14)
a15.Bind(wx.EVT_BUTTON,d15)
a17.Bind(wx.EVT_BUTTON,d17)
a18.Bind(wx.EVT_BUTTON,d18)



    
    

p.SetSizer(s)

frame.Show()
jisuanqi.MainLoop()
'''

