# -*- coding: cp936 -*-
#阅读器

book = raw_input('请输入文件名：')
b = open(book,'r')
while True:
    print '——————————输入数字1查看下一页，输入数字2退出阅读————————'.center(100)
    i = int(raw_input())
    if i == 1:
        for i in range(5):
            print b.readline()
    elif i == 2:
        break
        
b.close()
#E:\xuexi\Python\3.1\3.1_sql.py


