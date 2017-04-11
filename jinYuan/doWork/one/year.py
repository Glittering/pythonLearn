# -*- coding:UTF-8 -*-

#name = input("输入年月日，例如20170302:")
name = 20160522
print '输入的是：',name

last2 = name % 100
name = name / 100
mid2 = name % 100
name /= 100
for4 = name
print last2,mid2,name

# the input is due
# year
if (last2 >= 0 and last2 <100) and (mid2>=0 and mid2<100) and (for4>0 and for4<10000):
    pass
else:
    print '输入错误。'
    exit()
#month
if (mid2>0 and mid2<=12):
    pass
else:
    print 'input error month.'
    exit()

# the year is leap year
leap = False

if name % 100 !=0:
    if(name%4 == 0 and name % 100 != 0 ):
        leap = True
    else:
        pass
elif(name % 400):
    leap = True
else:
    pass

# dict of year
dictN = {1: 31, 2:28, 3:31, 4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#day
if last2>0 and last2<=dictN[mid2]:
    pass
else:
    print 'input error day'

#the all day
i=1
day=0
while(i<mid2):
    if i!=2 or (i==2 and leap==False):
        day += dictN[i]
    else:
        day += 29
    i+=1

print day + last2

