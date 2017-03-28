#coding:gbk
f=[]
def zip1(x,y):
    a=[]
    g=1
    b=[]
    c=0
   
    for i1 in x:
        a.append(i1)
    for i2 in y:
        b.append(i2)
    if len(a)>len(b):
        c=len(b)
    elif len(a)<=len(b):
        c=len(a)
      
    for i3 in a[0:c]:
        d=[]
        e=[]
        d.append(i3)
        
        for i4 in b[0:c]:
            d.append(i4)
        e.append(d[0])
        e.append(d[g])
        f.append(tuple(e))
        g+=1
zip1(x='123456',y='asdfghjkl')
print f

