#coding:gbk

import time,math

#1������ĳ��ĳ��ĳ�գ��ж���һ������һ��ĵڼ��죿
'''
a=time.mktime((2015,1,1,0,0,0,0,0,0),)
b=time.mktime((2015,5,20,0,0,0,0,0,0),)
print (b-a)/(3600*24)
'''

#2��쳲��������У�Fibonacci sequence�����ֳƻƽ�ָ����У�
#ָ��������һ�����У�0��1��1��2��3��5��8��13��21��34������
#�����������ַ���ʵ�֡�
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
3����ӡ������ͼ�������Σ�:
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
#4���������飬�������һ��Ԫ�ؽ�������С�������һ��Ԫ�ؽ�����������顣
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

#5�������������ļ�A��B,�����һ����ĸ,Ҫ����������ļ��е���Ϣ�ϲ�(����ĸ˳������), 
#�����һ�����ļ�C�С�
'''
a=open('C:\Users\�������\Desktop\B.txt','r')
b=open('C:\Users\�������\Desktop\A.txt','r')
c=open('C:\Users\�������\Desktop\C.txt','w')
d=a.read()+b.read()
e=''.join(sorted(d))
c.write(e)
c.close()
'''
#6��һ��������������100�ͼ���268����һ����ȫƽ���������ʸ����Ƕ��٣�
'''
a=1
while a:
    b=0
    if (b+100)//
'''
#7����һ��������5λ����������Ҫ��һ�������Ǽ�λ�������������ӡ����λ���֡�
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
#9����n��������ʹ��ǰ�����˳�������m��λ�ã����m���������ǰ���m����

m=3
n=[12,342,65,7687,214,5475,213,654,897,321]
for i in range(len(n)-m):
    n.append(n.pop(0))
print n
#10���ҵ����������ˣ�����������ҳ���������ʲô���⡣


if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print '%s,%d' % (m,person[m])
#��ǰ�ֵ�Ϊ��֪�ֵ䣬�ʿ����Լ�ȡֵ����Ϊδ֪�ֵ䣬����ҪԤ�Ȳ鿴��ֵ���Ҽ�ֵ����������δ�趨��Ĭ��Ϊ��������
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



    
    





























