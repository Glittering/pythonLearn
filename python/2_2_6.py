# -*- coding: utf-8 -*-

#去掉空字符串和none
def is_not_empty(s):
    return s and len(s.strip()) > 0
print  filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

#过滤出1~100中平方根是整数的数
import math

def is_sqr(x):
    return math.sqrt(x) % 1 == 0

print filter(is_sqr, range(1,101))
