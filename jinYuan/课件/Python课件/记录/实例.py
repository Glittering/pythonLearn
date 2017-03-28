#coding:gbk

'''
#空心正放心
for i in range(10):
    if i == 0 or i == 9:
        print '*' * 20

    else:
        print '*\t*'.expandtabs(19)
'''

#等腰梯形
'''
for i in range(3,10):
    if i == 3 or i == 5 or i == 7 or i == 9:
        print (i * '*').center(15)
'''
'''
a = 1
while a < 15:
    print (a * '*').center(30)
    a += 2
'''

#乘法口诀表
'''
for i in range(1,10):
    for j in range(1,i + 1):
        print '%d * %d = %-2d'%(j,i,i*j),
    print '\n'    
'''   


'''
1 * 1 
1 * 2  2 * 2
1 * 3  2 * 3  3 * 3
1 * 4  2 * 4  3 * 4  4 * 4


1  1
2  1,2
3  1,2,3
4  1,2,3,4
'''
'''
for i in range(1,10)[::-1]:
    for j in range(1,i + 1):
        print '%d * %d = %-2d'%(j,i,i*j),
    print '\n'   
'''
'''
for i in range(9,0,-1):
    for j in range(1,i + 1):
        print '%d * %d = %-2d'%(j,i,i*j),
    print '\n'  
'''

#石头剪刀布
'''
import random

guess_list = ['石头','剪刀','布']
vict_list = [('布','石头'),('石头','剪刀'),('剪刀','布')]

per_vic = 0
com_vic = 0

while True:
    com = random.choice(guess_list)
    per = raw_input('Please enter:')
    if per not in guess_list:
        per = raw_input('Please enter again:')
        continue

    if (com,per) in vict_list:
        print '电脑赢'
        com_vic += 1
        
    elif (per,com) in vict_list:
        print '玩家胜'
        per_vic += 1
        
    else:
        print '平局，请再来一局'

    if com_vic == 2:
        print '最终赢家：电脑'
        break
    if per_vic == 2:
        print '最终赢家：玩家'
        break
'''

l = [ 'keyman' , 'wisdom' , '1' , 100 , 20 , 1.1 , ['nes1' , 'nes2' , [ 'ness1' , 'ness2' ] ] ]
#l.remove('nes1')
#print l
a = l.index(['nes1' , 'nes2' , [ 'ness1' , 'ness2' ] ])
b = l[a].index('nes1')
'''
del l[a][b]   #l[-1][0]
print l
'''
'''
c = l.index(100)
l.pop(c)
print l
'''
#print l.remove(l(len(l-1)))
#print l[0:-1:2] 
#print l + [10,20,30]
l.extend(range(10,20,30)) 
#print l
d =  {'name':'keyman','age':26,'address':'beijing'}
#print d['phone_number']
#print d.get('phone_number',"key name 'phone_number' not in dictionary ")
#print d.pop('address')
#d.update(name = 'zhangsan')
d['name'] = 'zhangsan'
d.update(abc = 100)
d['aaa'] = 500
#print d

#列表推导式
'''
print [i for i in (1,2,3,4,5)]
print [i*5 for i in range(10) if i % 2 == 0]
'''
#斗地主发牌
'''
import random
l = range(10)
for i in range(5):
    random.shuffle(l)
    print l
'''

import random

cards = []
h = [chr(i) for i in range(3,7)]
s = range(2,11) + list('AJQK')
#print s
k = ['BOSS','boss']
for i in h:
    for j in s:
        cards.append('%s%s'%(i,j))
cards.extend(k)
#print len(cards)
random.shuffle(cards)

a = []
b = []
c = []

for x in range(17):
    a.append(cards.pop(0))
    b.append(cards.pop(0))
    c.append(cards.pop(0))
'''
print len(a)
print len(b)
print len(c)
'''
print '玩家一：',''.join(a)
print '玩家二：',''.join(b)
print '玩家三：',''.join(c)
print '底牌：',''.join(cards)
