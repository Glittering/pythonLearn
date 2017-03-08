# -*- coding:UTF-8 -*-

'''
get list of num
'''
print ('input num stop with -1:')
num = []
while(True):
    tmp = input('')
    if((tmp )!= -1):
        num.append(tmp)
    else:
        break
#num = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
print num

'''
get m
'''
m = input('input the num of m:')
#m=2     #移动位数

'''
the last char of m
'''
num1 = num[num.__len__()-2:]
#print num1

'''
the forwards of num
'''
num2 = num[:num.__len__()-2]
#print num2

'''
new num
'''
num = num1.__add__(num2)
print 'new num is:'+num