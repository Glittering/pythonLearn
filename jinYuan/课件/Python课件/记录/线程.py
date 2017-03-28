#coding:gbk

import wx
import codecs

#GetValue ��ȡֵ
#SetValue ����ֵ�����ǣ�
#AppendText ׷���ı�
#write ��ԭ�л�����д��


'''
class Mywx():
    def __init__(self):
        self.app = wx.App()
        self.frame = wx.Frame(None,size = (600,500))
        self.panel = wx.Panel(self.frame)
        
        self.filename = wx.TextCtrl(self.panel)
        self.content = wx.TextCtrl(self.panel,style = wx.TE_MULTILINE)

        self.op_butt = wx.Button(self.panel,label = "open")
        self.op_butt.Bind(wx.EVT_BUTTON,self.op)
        self.sa_butt = wx.Button(self.panel,label = "save")
        self.sa_butt.Bind(wx.EVT_BUTTON,self.sa)

        self.s_box = wx.BoxSizer()
        self.s_box.Add(self.filename,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box.Add(self.op_butt,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.s_box.Add(self.sa_butt,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        
        self.v_box = wx.BoxSizer(wx.VERTICAL)
        self.v_box.Add(self.s_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
        self.v_box.Add(self.content,proportion = 8,flag = wx.EXPAND|wx.ALL,border = 1)

        self.panel.SetSizer(self.v_box)

    def op(self,event):
        self.path = self.filename.GetValue()
        self.f = open(self.path,'r')
        self.content.SetValue(self.f.read())
        self.f.close()

    def sa(self,event):
        self.path = self.filename.GetValue()
        self.f = open(self.path,'a')
        self.f.write(self.content.GetValue())
        self.f.close()
        self.content.SetValue('')
        #self.content.AppendText('hello')
        #self.content.write('hello world')

        

a = Mywx()
a.frame.Show()
a.app.MainLoop()

'''


#python ���߳�

#���̣������һ�����У��ֳ�Ϊ����������

#�̣߳������µķ�֧���ֳ�Ϊ����������

#�첽����
    #ʱ��Ƭ

#GIL�����ƣ�ȫ�ֽ�������������֤ͬһ����ʱ��֮��ֻ��һ���߳�����


import thread
import threading
from time import sleep,ctime

'''
def loop0():
    print 'start loop0 at:',ctime()
    sleep(3)
    print 'loop0 done at:',ctime()

def loop1():
    print 'start loop1 at:',ctime()
    sleep(5)
    print 'loop1 done at:',ctime()

def main():
    print 'starting all at:',ctime()
    loop0()
    loop1()
    print 'all done at:',ctime()
    
main()
'''

'''
def loop0():
    print 'start loop0 at:',ctime()
    sleep(3)
    print 'loop0 done at:',ctime()

def loop1():
    print 'start loop1 at:',ctime()
    sleep(5)
    print 'loop1 done at:',ctime()

def main():
    print 'starting all at:',ctime()
    thread.start_new_thread(loop0,())  #-->loop0()
    thread.start_new_thread(loop1,())
    sleep(6)
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()

'''

'''
loops = [2,4,5] #����ȷ�����̵߳ĸ�������ȷ�������ĸ������̵߳�����ʱ��

def loop(nloop,nsec,lock):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()
    lock.release()

def main():
    print 'starting all at',ctime()
    locks = []
    nloops = range(len(loops))

    for i in nloops:
        l = thread.allocate_lock()
        l.acquire()
        locks.append(l)

    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
        
    sleep(5)
    print 'all done at:',ctime()
        
if __name__ == '__main__':
    main()

'''
'''
loops = [2,4] 

def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting all at',ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i]))  #�����߳�
        threads.append(t)
        
    for i in nloops:
        threads[i].start()  #��ʼִ���߳�
        #threads[i].setName('laoli')
        #print threads[i].isAlive()
        
    for i in nloops:
        #print threads[i].getName()
        threads[i].join() #�������ֱ���߳̽���
        #print threads[i].isAlive()

    print 'all done at:',ctime()
        
if __name__ == '__main__':
    main()

'''
'''
class Mythread(threading.Thread):
    def __init__(self,nloop,nsec):
        self.nloop = nloop
        self.nsec = nsec
        threading.Thread.__init__(self)

    def run(self):
        print 'start loop',self.nloop,'at:',ctime()
        sleep(self.nsec)
        print 'loop',self.nloop,'done at:',ctime()

if  __name__ == '__main__':
    loops = [2,4]
    nloops = range(len(loops))
    threads = []

    for i in nloops:
        t = Mythread(i,loops[i])
        threads.append(t)
        #threads[i].start()

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
'''
import sys,select

#print sys.argv
#print sys.stdin #��׼����
#sys.stdout ��׼���
#sys.stderr ��׼����


        
        
