#coding:gbk
import socket,time,thread,wx

class Server():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,title = "chat_server",size = (600,500))
        self.panel = wx.Panel(self.frame)

        self.chat_content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)
        self.message = wx.TextCtrl(self.panel)
        self.send_butt = wx.Button(self.panel,label = "����")
        self.send_butt.Bind(wx.EVT_BUTTON,self.send)

        self.s_box = wx.BoxSizer()
        self.s_box.Add(self.message,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 2)
        self.s_box.Add(self.send_butt,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 2)

        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.chat_content,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 2)
        self.v_box.Add(self.s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 2)

        self.panel.SetSizer(self.v_box)

    def sock(self):
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.bind(('',9109))
        self.soc.listen(3)
        self.con,self.add = self.soc.accept()
        while True:
            self.recvs = self.con.recv(1024)
            self.thetime = time.strftime("%Y-%m-%d %H:%M:%S")
            self.chat_content.write('�ͻ���' + self.thetime + '˵��\n')
            self.chat_content.write(self.recvs)
            self.chat_content.write('\n')

    def send(self,event):
        self.sends = self.message.GetValue()
        self.con.send(self.sends)
        self.message.SetValue('')
        self.thetime = time.strftime("%Y-%m-%d %H:%M:%S")
        self.chat_content.write(('�����%s˵��\n'%self.thetime).rjust(100))
        self.chat_content.write(self.sends)
        self.chat_content.write('\n')
        
    def start_thread(self):
        thread.start_new_thread(self.sock,())

if __name__ == "__main__":
    ser = Server()
    ser.start_thread()
    ser.frame.Show()
    ser.app.MainLoop()




