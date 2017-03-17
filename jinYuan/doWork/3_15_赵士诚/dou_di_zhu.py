#!/usr/bin/python3
#coding:utf-8
import random

a = range(1,14)
# print type(a)
# a = ''.join(a)     why??????why

b = ['a','b','c','d']

c=[]

for i in b:
    for k in a:
        c.append( i + str(k))


c.extend(['bk','lk'])
print c

random.shuffle(c)
print c
print 'FIRST :',
for i in range(12):
    print '%3s'%c.pop(0),
print
print 'SECOND:',
for i in range(12):
    # for i in range(12, 24):
    print '%3s'%c.pop(0),
print
print 'THIRD :',
# for i in range(24,36):
#     print c[i],
for i in range(12):
    print '%3s'%c.pop(0),
print
print 'FOURTH:',
# for i in range(36,48):
#     print c[i],
for i in range(12):
    print '%3s'%c.pop(0),
print

print 'REMAIN:',
for i in c:
    print '%3s'%i,