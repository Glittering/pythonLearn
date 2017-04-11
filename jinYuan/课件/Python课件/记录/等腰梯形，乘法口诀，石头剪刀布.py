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

