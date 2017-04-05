#!/usr/bin/python3

import wx

class Cacu():
    app = wx.App()
    frame = wx.Frame(None, title='Caculate')
    panel = wx.Panel(frame)
    s_box_content = wx.BoxSizer()
    v_box_num[4] = [wx.BoxSizer(wx.VERTICAL) for i in range(3)]
    s_box_bottom = wx.BoxSizer()
    my_button=''
    entered=''


    def __init__(self):
        pass


    def new_form():
        for i in range(17):
            #生成未绑定0-11 为数字0-9 和 .  = 后边为 + - * /  del  cle
            self.bt[i] = wx.Button(self.panel)
            self.my_button = '',i
            self.bt[i].Bind(wx.EVT_BUTTON, self.op)
        self.content = wx.TextCtrl(self.paner)


    def box_add():
        self.s_box_content.Add(self.content,proportion=10, flag=wx.EXPAND|wx.ALL, border=1)
        self.s_box_bottom()
        pass


    def set_value():
        self.content.SetValue(entered)


    def op(self, event):
        if self.my_button < '9' and self.my_button is not '':
            self.entered = self.entered , 'my_button'
            self.set_value()


if __name__ == '__main__':
    cacu = Cacu
    cacu.new_form()
