# coding:utf-8
# 1
for i in range(10):
    a = i
    while a:
        print '{}*{}={}'.format(i + 1 - a, i, i * (i + 1 - a)),
        a -= 1
        if (a < 1):
            print

# 4
a = range(0, 10)
a.reverse()
# print a
for i in a:
    b = 1
    while b <= i:
        print '{}*{}={}'.format(b, i, i * b),
        if b == i:
            print
        b += 1
# 1*9  2*9  3*9...

# 3  9*9 8*9 7*9
for i in a:
    b = i
    k = 9-i
    while k:
        print '%6s'%(""),
        k-=1
    while b:
        print '{}*{}=%2d'.format(b, i)%(b*i),
        b -= 1
        if b<1:
            print

#2  1*1   2*2  1*2
print
for i in range(1,10):
    k = 9-i
    # print k
    print ' '*k*7,
    # while k:
    #     print '%6s'%(''),
    #     k-=1
    b = i
    while b:
        print '{}*{}=%2d'.format(b, i) % (b * i),
        b-=1
        if b<1:
            print