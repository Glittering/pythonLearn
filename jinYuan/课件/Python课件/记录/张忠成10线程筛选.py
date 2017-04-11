#coding:gbk
import wx,re,thread,threading
from time import ctime,sleep

                 
                
                
def chazhao (event):
        a = lj.GetValue()
        b = open(a,'r')
        c = b.read()
        d = len(c)
        #for e in range(d):
               # if e == 1*(d/10) or e == 2*(d/10) or e == 3*(d/10) or e == 4*(d/10) or e == 5*(d/10) or e == 6*(d/10) or e == 7*(d/10) or e == 8*(d/10) or e == 9*(d/10) :
        main(c,d)



                

        
        
                
def tel0 (s):
        print 'tel0 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel0 finish:%s'%ctime()


def tel1 (s):
        print 'tel1 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel1 finish:%s'%ctime()
        


def tel2 (s):
        print 'tel2 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel2 finish:%s'%ctime()
        


def tel3 (s):
        print 'tel3 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel3 finish:%s'%ctime()
        


def tel4 (s):
        print 'tel4 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel4 finish:%s'%ctime()
        


def tel5 (s):
        print 'tel5 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel5 finish:%s'%ctime()
        


def tel6 (s):
        print 'tel6 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel6 finish:%s'%ctime()
        


def tel7 (s):
        print 'tel7 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel7 finish:%s'%ctime()
        


def tel8 (s):
        print 'tel8 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel8 finish:%s'%ctime()
        


def tel9 (s):
        print 'tel9 start:%s'%ctime()
        print re.findall(r'1[3]\d{8}',s)
        print re.findall(r'145\d{8}',s)
        print re.findall(r'15[012356789]\d{9}',s)
        print re.findall(r'170[05789]\d{7}',s)
        print re.findall(r'17[3678]\d{8}',s)
        print re.findall(r'18[02346789]\d{8}',s)
        print 'tel9 finish:%s'%ctime()
        




                                
def main (y,z):
        d = []
        for a in range(10):
                c1 = y[a*z/10:(a+1)*z/10]
                d.append(c1)
        a0 = [d.pop(0)]
        a1 = [d.pop(0)]
        a2 = [d.pop(0)]
        a3 = [d.pop(0)]
        a4 = [d.pop(0)]
        a5 = [d.pop(0)]
        a6 = [d.pop(0)]
        a7 = [d.pop(0)]
        a8 = [d.pop(0)]
        a9 = [d.pop(0)]


        print 'all starting at: %s'%ctime()
        threads = []
        t0 = threading.Thread(target = tel0,args = (a0))
        threads.append(t0)
        
        t1 = threading.Thread(target = tel1,args = (a1))
        threads.append(t1)
        
        t2 = threading.Thread(target = tel2,args = (a2))
        threads.append(t2)
        
        t3 = threading.Thread(target = tel3,args = (a3))
        threads.append(t3)
        
        t4 = threading.Thread(target = tel4,args = (a4))
        threads.append(t4)
        
        t5 = threading.Thread(target = tel5,args = (a5))
        threads.append(t5)
        
        t6 = threading.Thread(target = tel6,args = (a6))
        threads.append(t6)
        
        t7 = threading.Thread(target = tel7,args = (a7))
        threads.append(t7)
        
        t8 = threading.Thread(target = tel8,args = (a8))
        threads.append(t8)
        
        t9 = threading.Thread(target = tel9,args = (a9))
        threads.append(t9)
        print 'all over %s'%ctime()

        if __name__ == '__main__':
            for t in threads:
                t.setDaemon(True)
                t.start()

            print "all over %s" %ctime()
        




app = wx.App()
frame = wx.Frame(None,title = "筛选手机号",size = (600,500))
panel = wx.Panel(frame)

lj = wx.TextCtrl(panel,value = "1.txt")
sl = wx.TextCtrl(panel,value = "该类型数据数量：")
xx = wx.TextCtrl(panel)
cz = wx.Button(panel,label = "点\n击\n查\n找")
cz.Bind(wx.EVT_BUTTON,chazhao)

                
                

s_box = wx.BoxSizer(wx.VERTICAL)
s_box.Add(lj,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 4)
s_box.Add(sl,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 4)
s_box.Add(xx,proportion = 7,flag = wx.EXPAND|wx.ALL,border = 4)



h_box = wx.BoxSizer()
h_box.Add(s_box,proportion = 4,flag = wx.EXPAND|wx.ALL,border = 4)
h_box.Add(cz,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 4)

panel.SetSizer(h_box)





frame.Show()
app.MainLoop()
