#coding:gbk
import wx
import socket
import time
import thread
import sys
class server():
    title = 'python�������졪��������v1.0'#���ڵı���
    local='127.0.0.1'#ip��ַ
    port=9000#�˿ں�
    global serverSock #���ڴ���socket����
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
        #self.btn3.Bind(wx.EVT_BUTTON,self.daochu)
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
        #����socket����
        self.serverSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSock.bind((self.local,self.port))
        self.serverSock.listen(5)
        self.buffer = 1024
        self.jlname.AppendText('�������Ѿ�����......\n')
        #ѭ�����ܿͻ��˵���������
        while True:
            self.connection,self.address=self.serverSock.accept()
            self.flag= True
            #���տͻ��˷��͵���Ϣ
            while True:
                self.cienMsg=self.connection.recv(self.buffer)
                if not self.cienMsg:
                    continue
                elif self.cienMsg=='Y':
                    self.jlname.AppendText('�������Ѿ���ͻ��˽�������.......\n')
                    self.connection.send('Y')
                elif self.cienMsg=='N':
                    self.jlname.AppendText('��������ͻ��˽�������ʧ��.......\n')
                    self.connection.send('N')
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
                    self.jlname.AppendText('�ͻ��� '+theTime+' ˵��\n')
                    self.jlname.AppendText('  '+self.cienMsg+'\n')
    #������Ϣ
    def sendmessage(self,event):
        message=self.ltname.GetValue()
        theTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        self.jlname.AppendText('������ '+theTime+' ˵��\n')
        self.jlname.AppendText('   '+message+'\n')
        if self.flag==True:
            self.connection.send(message)
        else:
            self.jlname.AppendText('����δ��ͻ��˽������ӣ��ͻ����޷��յ�������Ϣ.....\n')
        self.ltname.Clear()
        
    def close(self,event):
        sys.exit()

    def startNewThread(self):
        thread.start_new_thread(self.receiveMessage,())
def main():
    ser=server()
    ser.startNewThread() 
    ser.app.MainLoop()
if __name__ == '__main__':
    main()

   


