#coding:gbk

import time,datetime,calendar

def dk (x):
      a = open(x,'r')
      return a
def dq (y):
      e = 10
      while e:
            print y.readline()
            e -= 1
      


b = raw_input('�������ļ�·����')

dk (b)
c = dk (b)
while 1:
      f = int(raw_input('�Զ���ҳ����1,�ֶ���ҳ����2��'))
      if f == 1:
            h = input('���뷭ҳ���ʱ�䣺')
            while 1:
                  dq (c)
                  time.sleep(h)
      elif f == 2:
            print '********ֱ�Ӱ�Enter����ҳ*******'
            while 1:
                  d = raw_input()
                  if d == '':
                       dq (c)
            else:
                  print '����1��ҳ��'
      else:
            print'���������룡�Զ���ҳ����1,�ֶ���ҳ����2��'
                  

