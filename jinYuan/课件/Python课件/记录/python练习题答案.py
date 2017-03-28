#coding:gbk

#1、
import time

#print time.mktime((y,m,d,0,0,0,0,0,0))[-2]

#2、
'''
def fb1(num):
    result = [1,1]
    for i in range(2,num):
        result.append(result[-1] + result[-2])
    return result
print fb1(10)
'''
'''
def fb2(num):
    result = []
    a = 1
    b = 1
    result.append(a)
    result.append(b)
    for i in range(2,num):
        a,b = b,a + b
        result.append(b)
    return result

print fb2(10)
'''
'''
result = [1,1]
def fb3(num):   
    if num == 1 or num == 2:
        return result
    else:
        result.append(result[-1] + result[-2])
        return fb3(num - 1)
    
print fb3(10)
'''

#3、
'''
for i in range(1,8,2):
    print ('*' * i).center(10)

for j in range(5,-1,-2):
    print ('*' * j).center(10)
'''
'''
import sys

for i in range(4):
    for j in range(2 - i + 1):
        sys.stdout.write(' ')
    for z in range(2 * i + 1):
        sys.stdout.write('*')
    sys.stdout.write('\n')

for i in range(3):
    for j in range(i + 1):
        sys.stdout.write(' ')
    for z in range(4 - 2 * i + 1):
        sys.stdout.write('*')
    sys.stdout.write('\n')
'''

#4、
'''
l1 = [10,1,55,23,66,88,30,3]
l2 = sorted(l1)

max_num = l2[-1]
min_num = l2[0]

max_num_index = l1.index(max_num)
min_num_index = l1.index(min_num)

l1[0],l1[max_num_index] = l1[max_num_index],l1[0]
l1[-1],l1[min_num_index] = l1[min_num_index],l1[-1]
print l1
'''


#6、
'''
import math

def demo():
    for i in range(10000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))

        if (x * x == i + 100) and (y * y == i + 268):
            print i

demo()

'''

#7、

num = raw_input('Please enter an integer:')
num = int(num)
'''
f = num / 10000
a = num % 10000 / 1000
b = num % 1000 /
c = b % 100
d = c % 10
'''
