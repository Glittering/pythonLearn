#!/usr/bin/python3

import wx

class Cacu():
    app = wx.App()
    frame = wx.Frame(None, title='Caculate')
    panel = wx.Panel(frame)
    s_box_content = wx.BoxSizer()
    s_box_num = [wx.BoxSizer() for i in range(3)]
    #wx.VERTICAL
    s_box_bottom_right = wx.BoxSizer()
    s_box_bottom = wx.BoxSizer()
    v_box_bottom_left = wx.BoxSizer(wx.VERTICAL)
    v_box_bottom_main = wx.BoxSizer(wx.VERTICAL)
    my_button=''
    entered=''
    bt = []


    def __init__(self):
        self.new_form()
        self.box_add()
        self.op()
        self.frame.Show()
        pass


    def new_form(self):
        print ('new_fowm is begin')
        for i in range(18):
            #生成未绑定0-11 为数字0-9 和 .  = 后边为 + - * /  del  cle
            self.bt[i] = wx.Button(self.panel,label='abc')
            self.my_button = '',i
            self.bt[i].Bind(wx.EVT_BUTTON, self.op)
        self.content = wx.TextCtrl(self.paner)
        print ('new_fowm is end')


    def box_add(self):
        print ('box_add is begin')
        self.s_box_content.Add(self.content,proportion=10, flag=wx.EXPAND|wx.ALL, border=1)

        for i in range [3]:
            self.s_box_num[0].Add(self.bt[ i+7 ],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
            pass
        # self.s_box_num[0].Add(self.bt[7],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        # self.s_box_num[0].Add(self.bt[8],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        # self.s_box_num[0].Add(self.bt[9],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_num[0].Add(self.bt[13],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)

        for i in range [3]:
            self.s_box_num[1].Add(self.bt[ i+4 ],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
            pass
        self.s_box_num[1].Add(self.bt[15],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)

        for i in range [3]:
            self.s_box_num[2].Add(self.bt[ i+1 ],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
            pass
        self.s_box_num[2].Add(self.bt[12],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)

        self.s_box_num[3].Add(self.bt[10],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_num[3].Add(self.bt[0],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_num[3].Add(self.bt[11],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_num[3].Add(self.bt[13],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)

        self.v_box_bottom_left.Add(self.s_box_num[0],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.v_box_bottom_left.Add(self.s_box_num[1],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.v_box_bottom_left.Add(self.s_box_num[2],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)
        self.v_box_bottom_left.Add(self.s_box_num[3],proportion=2.5, flag=wx.EXPAND|wx.ALL, border=1)

        self.s_box_bottom_right.Add(self.bt[16], proportion=6,flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_bottom_right.Add(self.bt[17], proportion=4,flag=wx.EXPAND|wx.ALL, border=1)

        self.s_box_bottom.Add(self.v_box_bottom_left, proportion=8,flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_bottom.Add(self.x_box_bottom_right, proportion=2,flag=wx.EXPAND|wx.ALL, border=1)

        self.v_box_bottom_main.Add(self.s_box_content, proportion=2,flag=wx.EXPAND|wx.ALL, border=1)
        self.v_box_bottom_main.Add(self.s_box_bottom, proportion=8,flag=wx.EXPAND|wx.ALL, border=1)

        self.panel.SetSizer(self.v_box_bottom_main)
        print ('box_add is end')



    def set_value(self):
        self.content.SetValue(entered)


    def op(self, event):
        print ('op is begin')
        if self.my_button < '9' and self.my_button is not '':
            self.entered = self.entered , 'my_button'
            self.set_value()
        print ('op is end')


if __name__ == '__main__':
    cacu = Cacu()
    cacu.app.MainLoop()
    # for i in range(3):
    #     print (i)
