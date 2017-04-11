#coding:gbk
import wx,socket,thread,time

class MyClient():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "Client",size = (500,400))
        self.panel = wx.Panel(self.frame)

        self.chat_content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)
        self.send_content = wx.TextCtrl(self.panel)
        self.send_button = wx.Button(self.panel,label = '发送')
        self.send_button.Bind(wx.EVT_BUTTON,self.send_message)

        self.s_box = wx.BoxSizer()
        self.s_box.Add(self.send_content,proportion = 4,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box.Add(self.send_button,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.chat_content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

        self.panel.SetSizer(self.v_box)

        

    def sock(self):
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.connect(('127.0.0.1',8001))

        while True:
            self.recvs = self.soc.recv(512)
            if self.recvs == 'Bye':
                self.thetime = time.strftime("%Y-%m-%d %H:%M:%S")
                self.chat_content.write('服务端' + self.thetime + '说：\n')
                self.chat_content.write(self.recvs)
                self.chat_content.write('\n')
                break
            else:
                self.thetime = time.strftime("%Y-%m-%d %H:%M:%S")
                self.chat_content.write('服务端' + self.thetime + '说：\n')
                self.chat_content.write(self.recvs)
                self.chat_content.write('\n')

    def send_message(self,event):
        self.sends = self.send_content.GetValue()
        self.soc.send(self.sends)
        
        self.thetime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.chat_content.write('客户端' + self.thetime + '说：\n')
        self.chat_content.write(self.sends)
        self.chat_content.write('\n')
        
        self.send_content.SetValue('')

    def new_thread(self):
        thread.start_new_thread(self.sock,())
        
if __name__ == '__main__':
    c = MyClient()
    c.new_thread()
    c.frame.Show()
    c.app.MainLoop()
