#coding:gbk


import time
a=raw_input('������Ҫ�򿪵��ļ�·��')
b=open(a,'r')
tj=int(raw_input('����1���Զ�����2���ֶ��������ڷ�ҳģʽ'))
if tj == 2:
    num=int(raw_input('����Ҫ��ת������'))
    while True:
        FY=raw_input()
        print b.readline()
        num-=1
elif tj==1:
    num1=int(raw_input('���뷭ҳ������'))
    num=int(raw_input('���뷭ҳ�ļ��ʱ�䣨�룩'))
    while num:
        while num1:
            print b.readline()
            time.sleep(num)
            


