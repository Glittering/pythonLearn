#coding:gbk
import codecs,wx,time

class Myreader():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "our_reader",size = (600,500))
        self.panel = wx.Panel(self.frame)

        self.filename = wx.TextCtrl(self.panel)
        self.open_file = wx.Button(self.panel,label = '打开')
        self.open_file.Bind(wx.EVT_BUTTON,self.op)

        self.content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)

        self.auto_bt = wx.Button(self.panel,label = "Auto")
        self.auto_bt.Bind(wx.EVT_BUTTON,self.auto)
        self.manual_bt = wx.Button(self.panel,label = "Manual")
        self.manual_bt.Bind(wx.EVT_BUTTON,self.manual)

        self.top_box = wx.BoxSizer()
        self.top_box.Add(self.filename,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.top_box.Add(self.open_file,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 1)

        self.bottom_box = wx.BoxSizer()
        self.bottom_box.Add(self.auto_bt,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.bottom_box.Add(self.manual_bt,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.top_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.content,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.bottom_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        
        self.panel.SetSizer(self.v_box)

    def op(self,event):
        self.path = self.filename.GetValue()
        #self.f = open(self.path,'r')
        self.f = codecs.open(self.path,'r','gbk')
        self.content.write(self.one_page())

    def one_page(self):
        return self.f.read(800)

    def auto(self,event):
            while True:
                self.content.SetValue('')
                self.content.write(self.one_page())
                time.sleep(3)

    def manual(self,event):
        self.content.SetValue('')
        self.content.write(self.one_page())

if __name__ == '__main__':
    a = Myreader()
    a.frame.Show()
    a.app.MainLoop()
    
