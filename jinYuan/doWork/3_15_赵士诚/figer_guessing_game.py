#!/usr/bin/python3
#coding:utf-8
import random


def compare(enter):
    com_enter=random.choice([1,2,3])
    if com_enter == enter:
        print 'same'
    elif com_enter == enter+1 or com_enter == 1 and enter == 3:
        print 'you lose,the computer is{}'.format(com_enter)
    else:
        print 'you won,the computer is{}'.format(com_enter)


while(1):
    enter = input('enter,1,2,3 for 剪刀，石头，布')
    compare(enter)