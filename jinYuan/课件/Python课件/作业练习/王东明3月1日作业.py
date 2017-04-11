#coding:gbk


import time
a=raw_input('请输入要打开的文件路径')
b=open(a,'r')
tj=int(raw_input('输入1（自动）或2（手动）来调节翻页模式'))
if tj == 2:
    num=int(raw_input('输入要跳转的行数'))
    while True:
        FY=raw_input()
        print b.readline()
        num-=1
elif tj==1:
    num1=int(raw_input('输入翻页的行数'))
    num=int(raw_input('输入翻页的间隔时间（秒）'))
    while num:
        while num1:
            print b.readline()
            time.sleep(num)
            


