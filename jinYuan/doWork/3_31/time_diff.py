#!/usr/bin/python3

import time

y = input('enter year:')
# print (type(y))

m = input('enter month:')

d = input('enter day:')

ti = y + m + d

t = time.strptime(ti,"%Y%m%d")

# print (time.time()-time.mktime(t))

dif = time.time()-time.mktime(t)

dif = int(dif)

day = dif / 3600

print (int(day))
