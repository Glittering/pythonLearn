 #coding:gbk
import wx
import socket
import time
import thread
import sys
class client():
    title = 'python在线聊天——客户端v1.0'#窗口的标题
    local='127.0.0.1'#ip地址
    port=9000#端口号
    global clientSock #用于创建socket对象
    flag =False#判断是否连接客户端
    #初始化一个窗口
    def __init__(self):
        self.app=wx.App()#实例化一个wx主循环
        #创建一个窗体
        self.win=wx.Frame(None,title=self.title,size=(410,335))
        #创建画布
        self.panel=wx.Panel(self.win)
        #发送按钮
        self.btn1=wx.Button(self.panel,label='发送')
        self.btn1.Bind(wx.EVT_BUTTON,self.sendmessage)
        #退出按钮
        self.btn2=wx.Button(self.panel,label='退出')
        self.btn2.Bind(wx.EVT_BUTTON,self.close)
        #导出聊天记录按钮
        self.btn3=wx.Button(self.panel,label='导出聊天记录')
        #聊天消息写入窗口
        self.ltname=wx.TextCtrl(self.panel)
        #聊天记录查看窗口
        self.jlname=wx.TextCtrl(self.panel,style=wx.TE_MULTILINE|wx.HSCROLL)
        #创建水平方向尺寸器
        self.s_box=wx.BoxSizer()
        #水平方向尺寸器包含的组件
        self.s_box.Add(self.btn1,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        self.s_box.Add(self.btn2,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        self.s_box.Add(self.btn3,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        #创建垂直方向尺寸器
        self.v_box=wx.BoxSizer(wx.VERTICAL)
        #垂直方向尺寸器所包含的组件
        self.v_box.Add(self.jlname,proportion=5,flag=wx.EXPAND|wx.ALL,border=1)
        self.v_box.Add(self.ltname,proportion=2,flag=wx.EXPAND|wx.ALL,border=1)
        self.v_box.Add(self.s_box,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        #声明主尺寸器
        self.panel.SetSizer(self.v_box)
        #显示窗口
        self.win.Show()
    #接收消息的函数
    def receiveMessage(self):
        try:
            #建立socket连接
            self.clientSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.clientSock.connect((self.local,self.port))
            self.flag = True
        except:
            self.flag=False
            self.jlname.AppendText('您还未与服务器建立连接，请检查服务器端是否已经启动....\n')
            return
        self.buffer = 1024
        self.clientSock.send('Y')
        #循环接受客户端的连接请求
            #接收客户端发送的消息
        while True:
            try:
                if self.flag == True:
                    self.serverMsg=self.clientSock.recv(self.buffer)
                    if self.serverMsg=='Y':
                        self.jlname.AppendText('客户端已经与服务器建立连接.......\n')
                    elif self.serverMsg=='N':
                        self.jlname.AppendText('客户端与服务器建立连接失败.......\n')
                    elif not self.serverMsg:
                        continue
                    else:
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                        self.jlname.AppendText('服务器端 '+theTime+' 说：\n')
                        self.jlname.AppendText('  '+self.serverMsg+'\n')
                else:
                    break
            except EOFError,msg:
                raise msg
                self.clientSock.colse()
                break
    def sendmessage(self,event):
        message=self.ltname.GetValue()
        theTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.jlname.AppendText('客户端 '+theTime+' 说：\n')
        self.jlname.AppendText('   '+message+'\n')
        if self.flag==True:
            self.clientSock.send(message)
        else:
            self.jlname.AppendText('您还未与服务器端建立连接，服务器端无法收到您的消息.....\n')
        self.ltname.Clear()

    def close(self,event):
        sys.exit()
    def startNewThread(self):
        thread.start_new_thread(self.receiveMessage,())


def main():
    cli=client()
    cli.startNewThread() 
    cli.app.MainLoop()

main()

