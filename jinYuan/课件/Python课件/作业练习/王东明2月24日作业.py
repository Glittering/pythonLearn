#coding:gbk
#for i in range(10):
#    print "*" * i


#for i1 in range(5,10):
#    print ' ' *(10-i1), '*' * i1*2
'''    
for i2 in range(21):
    if i2==0:
        print ' *' * 20
    elif i2==20:
        print ' *' * 20
    elif i2==10:
        print '*',14* ' ',"王东明",' '*14 ,'*'
    else:
        print '*',36*' ','*'
'''
'''
range(1,10)[::-1]
for i3 in range(1,10):
    for i4 in range(1,i3+1):
        print i4,'*',i3,'=',i3*i4,
    print '\n'
for i3 in range(1,10)[::-1]:
    for i4 in range(1,i3+1)[::-1]:
         print i4,'*',i3,'=',i3*i4,
    print '\n'
'''
# 第二三象限如何写？
# 为什么用raw_input()就行用str(input())就不行?
s=1
s3='石头'
s4='剪刀'
s5='布'
wanjia=0
diannao=0
while s:
    import random
    guess_list=[s5,s3,s4]
    AI=random.choice(guess_list)
    use = raw_input("石头？剪刀？布\n")
    if use==s3:
        if AI==s3:
            print AI,'平手，再来'
        elif AI==s4:
            print AI,'你赢了'
            wanjia=wanjia+1
        elif AI==s5:
            print AI,'我赢了'
            diannao=diannao+1
    elif use==s4:
         if AI==s3:
            print AI,'我赢了'
            diannao=diannao+1
         elif AI==s4:
            print AI,'平手，再来'
         elif AI==s5:
            print AI,'你赢了'
            wanjia=wanjia+1
    elif use==s5:
        if AI==s3:
            print AI,'你赢了'
            wanjia=wanjia+1
        elif AI==s4:
            print AI,'我赢了'
            diannao=diannao+1
        elif AI==s5:
            print AI,'平手，再来'
    else:
        print '这个不算'
     
    if wanjia==3 and wanjia>diannao:
        print '你赢了'
        s=0
    elif diannao==3 and diannao>wanjia:
        print '你输了'
        s=0
    
