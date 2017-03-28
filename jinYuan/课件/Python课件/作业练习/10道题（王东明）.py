#coding:gbk

import time,math

#1、输入某年某月某日，判断这一天是这一年的第几天？
'''
a=time.mktime((2015,1,1,0,0,0,0,0,0),)
b=time.mktime((2015,5,20,0,0,0,0,0,0),)
print (b-a)/(3600*24)
'''

#2、斐波那契数列（Fibonacci sequence），又称黄金分割数列，
#指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
#请用至少三种方法实现。
'''
a=[1,1]
for i in range(10):
    
    a.append(a[-1]+a[-2])
    
print a
  
'''
'''
a=[1,1]
b=10
while b:
    a.append(a[-1]+a[-2])
    b-=1
print a
'''
'''
a=[1,1]
def fb(b):
    if b==0:
        return a
    else:
        c=a[-1]+a[-2]
        a.append(c)
        return fb(b-1)
print fb(10)

'''
'''
3、打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''
'''
for i in range(4):
    a=2*i+1
    b=3-i
    c=''*b+'*'*a
    print c.center(7)
 
for j in range(3):
    d=5-2*j
    e=j+1
    f=''*e+'*'*d
    print f.center(7)

'''
#4、输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''
a=[2,1,3,4,5,6,9,8,7,11,10]
b=sorted(a)
c=a.index(b.pop())
a.insert(c-1,a.pop(0))
a.insert(0,(a.pop(c)))
d=a.index(b.pop(0))
a.insert(d,a.pop())
a.append(a.pop(d+1))
print a

'''

#5、有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 
#输出到一个新文件C中。
'''
a=open('C:\Users\异乡异客\Desktop\B.txt','r')
b=open('C:\Users\异乡异客\Desktop\A.txt','r')
c=open('C:\Users\异乡异客\Desktop\C.txt','w')
d=a.read()+b.read()
e=''.join(sorted(d))
c.write(e)
c.close()
'''
#6、一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？
'''
a=1
while a:
    b=0
    if (b+100)//
'''
#7、给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
a=12345
b=str(a)
c=' '.join(b)
d=c.split(' ')
print len(b)
e=[]
for i in range(len(d)):
    x=len(d)-1-i
    print d[x]
'''
'''
#9、有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

m=3
n=[12,342,65,7687,214,5475,213,654,897,321]
for i in range(len(n)-m):
    n.append(n.pop(0))
print n
#10、找到年龄最大的人，并输出。请找出程序中有什么问题。


if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print '%s,%d' % (m,person[m])
#当前字典为已知字典，故可以以键取值，若为未知字典，则需要预先查看键值表，且键值的数据属性未设定，默认为整形数。
    m=person[0]
    for jian in person.keys():
        if int(person[m])<int(person[jian]):
            m=person[jian]
        elif:int(person[m])=int(person[jian]):
            m=person[jian]
    print '%s%d'%(m,person[m])


'''


m=3
n=[12,342,65,7687,214,5475,213,654,897,321]
N=[]
for i in range(m):
    N.append(n.pop(0))
for i in range(m):
    n.insert(0,n.pop(len(n)-2))
for i in range(m):
    n.append(N.pop(0))
print n



    
    





























