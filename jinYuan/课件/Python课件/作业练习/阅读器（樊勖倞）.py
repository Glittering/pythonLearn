# -*- coding: cp936 -*-
#�Ķ���

book = raw_input('�������ļ�����')
b = open(book,'r')
while True:
    print '����������������������������1�鿴��һҳ����������2�˳��Ķ�����������������'.center(100)
    i = int(raw_input())
    if i == 1:
        for i in range(5):
            print b.readline()
    elif i == 2:
        break
        
b.close()
#E:\xuexi\Python\3.1\3.1_sql.py


