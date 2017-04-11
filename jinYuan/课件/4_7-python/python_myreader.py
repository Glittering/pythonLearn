#coding:gbk

import wx,time,codecs


class Myreader():
    
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "myreader")
        self.panel = wx.Panel(self.frame)

        self.filename = wx.TextCtrl(self.panel)
        self.open_button = wx.Button(self.panel,label = "open")
        self.open_button.Bind(wx.EVT_BUTTON,self.op)

        self.s_box_top = wx.BoxSizer()
        self.s_box_top.Add(self.filename,proportion = 4,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box_top.Add(self.open_button,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        
        self.content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE|wx.HSCROLL)

        self.auto = wx.Button(self.panel,label = "auto")
        self.auto.Bind(wx.EVT_BUTTON,self.zidong)
        self.manual = wx.Button(self.panel,label = "manual")
        self.manual.Bind(wx.EVT_BUTTON,self.shou)

        self.s_box_bottom = wx.BoxSizer()
        self.s_box_bottom.Add(self.auto,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box_bottom.Add(self.manual,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.s_box_top,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.content,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.s_box_bottom,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.panel.SetSizer(self.v_box)
        self.frame.Show()
        self.app.MainLoop()
    def op(self,event):
        self.path = self.filename.GetValue()
        #self.f = open(self.path,'r')
        self.f = codecs.open(self.path,'r','gbk')
        self.content.SetValue(self.f.read(800))
        self.read()
        self.autoread = 1
        #self.f.close()

    def read(self):
        self.content.SetValue('')
        self.content.write(self.f.read(800))

    def zidong(self,event):
        self.autoread = 1
        while self.autoread:
            self.read()
            time.sleep(3)
    def shou(self,event):
        self.read()
        
        
            
if __name__ == '__main__':
    a = Myreader()

