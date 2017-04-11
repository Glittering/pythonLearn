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
      


b = raw_input('请输入文件路径：')

dk (b)
c = dk (b)
while 1:
      f = int(raw_input('自动翻页输入1,手动翻页输入2：'))
      if f == 1:
            h = input('输入翻页间隔时间：')
            while 1:
                  dq (c)
                  time.sleep(h)
      elif f == 2:
            print '********直接按Enter键翻页*******'
            while 1:
                  d = raw_input()
                  if d == '':
                       dq (c)
            else:
                  print '输入1翻页：'
      else:
            print'请重新输入！自动翻页输入1,手动翻页输入2：'
                  

