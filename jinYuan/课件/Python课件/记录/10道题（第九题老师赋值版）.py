# coding:utf8
'''
class nToM():
    def __init__(self,dList):
        self.sList = dList

        for _ in range(0,3):
            self.sList.append(self.sList.pop(0))
        print self.sList

if __name__ == '__main__':

    aList = [1,2,3,4,5,6,7]
    n = nToM(aList)
'''

if __name__ == '__main__':
    n = input('Please enter the total number:')
    m = input('Please enter:')

    def move(l,n,m):
        l_end = l[n - 1]
        for i in range(n-1,-1,-1):
            l[i] = l[i - 1]
        l[0] = l_end
        m -= 1
        
        if m > 0:
            move(l,n,m)
             

    l = []
    for i in range(n):
        num = input('Please enter the number:')
        l.append(num)
    print l
    move(l,n,m)
    print l

#[10,20,30,40,50]
'''
[10,20,30,40,40]
[10,20,30,30,40]
[10,20,20,30,40]
[50,10,20,30,40]
'''
