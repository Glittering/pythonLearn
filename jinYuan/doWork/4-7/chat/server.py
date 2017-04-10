import wx, socket, thread, time

class Myserver():
    def __init__(self):
        self.app = wx.App()
	self.frame = wx.Frame(None, title='Server', size=(500,400))
	self.panel = wx.Panel(self.frame)

	self.chat_content = wx.TextCtrl(self.panel)
	self.send_content = wx.TextCtrl(self.panel)
        self.send_button  = wx.Button(self.panel)

	self.s_box = wx.BoxSizer()
	self.s_box.Add(self.send_content, proportion=4, flag=wx.EXPAND|wx.ALL, border=1)
	self.s_box.Add(self.send_button, proportion=1, flag=wx.EXPAND|wx.ALL, border=1)
	
	self.v_box = wx.BoxSizer(wx.VERTICAL)
	self.v_box.Add(self.chat_content, proportion=9, flag=wx.EXPAND|wx.ALL,border=1)
	self.v_box.Add(self.s_box, proportion=9, flag=wx.EXPAND|wx.ALL,border=1)

	self.paner.SetSizer(slef.v_box)

	self.frame.Show()
	self.app.MainLoop()


    def sock(self):
        self.soc
