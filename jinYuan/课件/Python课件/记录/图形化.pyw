#coding:gbk
import wx

'''
app = wx.App() #ʵ����һ��Ӧ�ó�����ѭ����
frame = wx.Frame(None) #ʵ����һ���������
frame.Show()   #���ô����������ʾ����
app.MainLoop() #������ѭ��
'''
'''
app = wx.App() 
frame = wx.Frame(None)

frame.Show() 
app.MainLoop()
'''


#Frame ����
    #parent ���������ΪNoneʱ��������Ϊ�������
    #id     ��ţ�������ı�ʶ��ͬһͼ�λ����浱�в��ܳ���id��ͬ�������
            #��idΪ-1ʱ����������Զ�����id
    #title  ���⣬���ڵı���
    #pos    �����λ�ã���Ҫһ��˫Ԫ��Ԫ�飬�γ�����ϵ�����涨�������;��ϵľ���
    #size   ����Ĵ�С����Ҫһ��˫Ԫ��Ԫ�飬���涨����Ŀ�͸�
    #style  �������ʽ
    #name   ���֣�������ı�ʶ

#Button ��ť
    #label  ��ť�ϵ�����

#TextCtrl �ı������
    #value  �ı���������������

'''
app = wx.App()
frame = wx.Frame(None,title = "hello",size = (410,335))

bt1 = wx.Button(frame,label = "open",pos = (225,5),size = (80,25))
#bt2 = wx.Button(frame,label = "save",pos = (315,5),size = (80,25))

#filename = wx.TextCtrl(frame,pos = (5,5),size = (210,25))
#content = wx.TextCtrl(frame,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE|wx.HSCROLL)

frame.Show()
app.MainLoop()
'''

#�ߴ�������
    #Panel ���������ڵ�����
    #1�������ߴ���
        #BoxSizer
            #Ĭ��Ϊˮƽ�ߴ���
            #��ֱ�ߴ���
                #wx.VERTICAL
    #2��������
        #Add
            #proportion ����
            #flag
                #������ʽ
                    #wx.EXPAND 
                #���ķ���  --> �߿�
                    #wx.TOP
                    #wx.BOTTOM
                    #wx.LEFT
                    #wx.RIGHT
                    #wx.ALL

            #border �߿�

    #3���������ߴ���
        #SetSizer
'''

app = wx.App()
frame = wx.Frame(None,title = "hello",size = (410,335))
panel = wx.Panel(frame)

bt1 = wx.Button(panel,label = "open")
bt2 = wx.Button(panel,label = "save")

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel,style = wx.TE_MULTILINE|wx.HSCROLL)

h_box = wx.BoxSizer()
h_box.Add(filename,proportion = 8,flag = wx.EXPAND|wx.LEFT,border = 1)
h_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
h_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)

frame.Show()
app.MainLoop()  

'''

#���¼�
    #event
    #Bind
        #wx.EVT_BUTTON ��ť�¼����ܳ�
    #GetValue ��ȡֵ
    #SetValue ����ֵ

def dk(event):
    path = filename.GetValue()
    f = open(path,'r')
    content.SetValue(f.read())
    f.close()


app = wx.App()
frame = wx.Frame(None,title = "hello",size = (410,335))
panel = wx.Panel(frame)

bt1 = wx.Button(panel,label = "open")
bt1.Bind(wx.EVT_BUTTON,dk)
bt2 = wx.Button(panel,label = "save")

filename = wx.TextCtrl(panel)
content = wx.TextCtrl(panel,style = wx.TE_MULTILINE)
 
h_box = wx.BoxSizer()
h_box.Add(filename,proportion = 8,flag = wx.EXPAND|wx.LEFT,border = 1)
h_box.Add(bt1,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
h_box.Add(bt2,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)

v_box = wx.BoxSizer(wx.VERTICAL)
v_box.Add(h_box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 1)
v_box.Add(content,proportion = 9,flag = wx.EXPAND|wx.ALL,border = 1)

panel.SetSizer(v_box)

frame.Show()
app.MainLoop()  


