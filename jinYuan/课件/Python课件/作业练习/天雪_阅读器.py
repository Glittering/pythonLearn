#！coding:gbk

import time
f = open('1.txt','r')

a = raw_input('输入"自动阅读"或者"手动阅读":')
if a == '自动阅读':
    while True:
        f.seek(0,1)
        print f.read(100)
        time.sleep(3)
elif a == '手动阅读':
    
    print f.read(100)
    while True:
        b = raw_input('输入"上一页"或者"下一页":')
        if b == '上一页':
            f.seek(-200,1)
            '''
            if f.tell()<208 and f.tell()>100:
                f.seek(0,0)
                print f.read(100)
            elif f.tell() == 208:
                print '已经是第一页'
            '''
            
            print f.read(100)    
        elif b == '下一页':
            f.seek(0,1)
            print f.read(100)
            
f.close()
