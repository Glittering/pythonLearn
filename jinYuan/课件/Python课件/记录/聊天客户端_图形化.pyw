 #coding:gbk
import wx
import socket
import time
import thread
import sys
class client():
    title = 'python�������졪���ͻ���v1.0'#���ڵı���
    local='127.0.0.1'#ip��ַ
    port=9000#�˿ں�
    global clientSock #���ڴ���socket����
    flag =False#�ж��Ƿ����ӿͻ���
    #��ʼ��һ������
    def __init__(self):
        self.app=wx.App()#ʵ����һ��wx��ѭ��
        #����һ������
        self.win=wx.Frame(None,title=self.title,size=(410,335))
        #��������
        self.panel=wx.Panel(self.win)
        #���Ͱ�ť
        self.btn1=wx.Button(self.panel,label='����')
        self.btn1.Bind(wx.EVT_BUTTON,self.sendmessage)
        #�˳���ť
        self.btn2=wx.Button(self.panel,label='�˳�')
        self.btn2.Bind(wx.EVT_BUTTON,self.close)
        #���������¼��ť
        self.btn3=wx.Button(self.panel,label='���������¼')
        #������Ϣд�봰��
        self.ltname=wx.TextCtrl(self.panel)
        #�����¼�鿴����
        self.jlname=wx.TextCtrl(self.panel,style=wx.TE_MULTILINE|wx.HSCROLL)
        #����ˮƽ����ߴ���
        self.s_box=wx.BoxSizer()
        #ˮƽ����ߴ������������
        self.s_box.Add(self.btn1,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        self.s_box.Add(self.btn2,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        self.s_box.Add(self.btn3,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        #������ֱ����ߴ���
        self.v_box=wx.BoxSizer(wx.VERTICAL)
        #��ֱ����ߴ��������������
        self.v_box.Add(self.jlname,proportion=5,flag=wx.EXPAND|wx.ALL,border=1)
        self.v_box.Add(self.ltname,proportion=2,flag=wx.EXPAND|wx.ALL,border=1)
        self.v_box.Add(self.s_box,proportion=1,flag=wx.EXPAND|wx.ALL,border=1)
        #�������ߴ���
        self.panel.SetSizer(self.v_box)
        #��ʾ����
        self.win.Show()
    #������Ϣ�ĺ���
    def receiveMessage(self):
        try:
            #����socket����
            self.clientSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.clientSock.connect((self.local,self.port))
            self.flag = True
        except:
            self.flag=False
            self.jlname.AppendText('����δ��������������ӣ�������������Ƿ��Ѿ�����....\n')
            return
        self.buffer = 1024
        self.clientSock.send('Y')
        #ѭ�����ܿͻ��˵���������
            #���տͻ��˷��͵���Ϣ
        while True:
            try:
                if self.flag == True:
                    self.serverMsg=self.clientSock.recv(self.buffer)
                    if self.serverMsg=='Y':
                        self.jlname.AppendText('�ͻ����Ѿ����������������.......\n')
                    elif self.serverMsg=='N':
                        self.jlname.AppendText('�ͻ������������������ʧ��.......\n')
                    elif not self.serverMsg:
                        continue
                    else:
                        theTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                        self.jlname.AppendText('�������� '+theTime+' ˵��\n')
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
        self.jlname.AppendText('�ͻ��� '+theTime+' ˵��\n')
        self.jlname.AppendText('   '+message+'\n')
        if self.flag==True:
            self.clientSock.send(message)
        else:
            self.jlname.AppendText('����δ��������˽������ӣ����������޷��յ�������Ϣ.....\n')
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

