#coding:gbk

import wx,thread,re,threading
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
        
        self.xx=wx.TextCtrl(self.p,style=wx.TE_MULTILINE)
        self.xr=wx.TextCtrl(self.p,style=wx.TE_MULTILINE)
        self.fs=wx.Button(self.p,label='搜索')
        self.fs.Bind(wx.EVT_BUTTON,self.duoxiancheng)
        
        self.h=wx.BoxSizer()
        self.h1=wx.BoxSizer()
        self.s=wx.BoxSizer(wx.VERTICAL)
        
        self.h.Add(self.xx,proportion=5,flag=wx.EXPAND|wx.ALL,border=1)
        self.h1.Add(self.xr,proportion=4,flag=wx.EXPAND|wx.ALL,border=1)
        self.h1.Add(self.fs,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        
        self.s.Add(self.h,proportion=6,flag=wx.EXPAND|wx.ALL,border=1)
        self.s.Add(self.h1,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        
        self.p.SetSizer(self.s)

    def dakai(self):
        self.path=self.xr.GetValue()
        self.nr = open(self.path,'r')
        self.dq=self.nr.read()
    def dakai1(self): 
        self.e1=re.findall(r'/d',self.dq[:(len(self.dq))/10])
        
    def dakai2(self):   
        self.e2=re.findall(r'/d',self.dq[(len(self.dq))/10:(len(self.dq))/5])
        
    def dakai3(self):
        self.e3=re.findall(r'/d',self.dq[(len(self.dq))/5:(len(self.dq))*3/10])
        
    def dakai4(self):
        self.e4=re.findall(r'/d',self.dq[(len(self.dq))*3/10:(len(self.dq))*2/5])
        
    def dakai5(self):
        self.e5=re.findall(r'/d',self.dq[(len(self.dq))*2/5:(len(self.dq))/2])
        
    def dakai6(self):
        self.e6=re.findall(r'/d',self.dq[(len(self.dq))/2:(len(self.dq))*3/5])
        
    def dakai7(self):
        self.e7=re.findall(r'/d',self.dq[(len(self.dq))*3/5:(len(self.dq))*7/10])
        
    def dakai8(self):
        self.e8=re.findall(r'/d',self.dq[(len(self.dq))*7/10:(len(self.dq))*4/5])
        
    def dakai9(self):
        self.e9=re.findall(r'/d',self.dq[(len(self.dq))*4/5:(len(self.dq))*9/10])
        
    def dakai10(self):
        self.e10=re.findall(r'/d',self.dq[(len(self.dq))*9/10:])

        
    def duoxiancheng(self,event):
        self.D=[self.dakai1,self.dakai2,self.dakai3,self.dakai4,self.dakai5,self.dakai6,self.dakai7,self.dakai8,self.dakai9,self.dakai10]
        
        for i in range(len(self.D)):
            self.D[i].start()
            
        for i in range(len(self.S)):
            self.D[i].join()
            
        self.E=''.join(self.e1)+''.join(self.e2)+''.join(self.e3)+''.join(self.e4)+''.join(self.e5)+''.join(self.e6)+''.join(self.e7)+''.join(self.e8)+''.join(self.e9)+''.join(self.e10)
        self.F=[]
        self.F.append(re.findall(r'139/d{8}',self.E))
        for i in range(len(self.F)):
            print self.F[i],'\n'
            print '共有',len(self.F)-1,'个电话号码'
            
            


if __name__=='__main__':
    u=user()
    u.f.Show()
    u.a.MainLoop()


