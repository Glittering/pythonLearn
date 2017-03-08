# -*- coding:UTF-8 -*-

def fb(len):
    if len == 0:
        print 'input error'
        ifDue(getLen())
    else:
        pass
    a = 0
    b = 1
    c = 2
    while(c<len):
        b+=a
        a=b-a
        c+=1
    print b

def ifDue(len):
    if len<2:
        return 0
    else:
        return len

def getLen():
    len = input('input a num,that is more than 2:')
    return len


fb(ifDue(getLen()))
