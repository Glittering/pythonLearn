import random
s=1
while s:
    a=[]
    b=[]
    for i in range(48,58):
        a.append(chr(i))
    for i in range(65,91):
        a.append(chr(i))
    for i in range(97,123):
        a.append(chr(i))
    for i in range(6):
        b.append(random.choice(a))
    print b
    print str(b)
    c=raw_input()
    
    if c==''.join(b):
        s=0
        print '正确'
    else:
        print '请重新输入'
        
