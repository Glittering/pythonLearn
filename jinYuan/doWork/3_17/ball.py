#!/usr/lib/python
#coding:utf-8

def hight(long_t):
    long_t = float(long_t)
    long = 0.0
    if long_t < 0.5:
        return 0.0
    else :
        long += hight(long_t / 2) + long_t/2 + long_t
    return long
print hight(100)