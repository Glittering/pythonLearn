#��coding:gbk

import time
f = open('1.txt','r')

a = raw_input('����"�Զ��Ķ�"����"�ֶ��Ķ�":')
if a == '�Զ��Ķ�':
    while True:
        f.seek(0,1)
        print f.read(100)
        time.sleep(3)
elif a == '�ֶ��Ķ�':
    
    print f.read(100)
    while True:
        b = raw_input('����"��һҳ"����"��һҳ":')
        if b == '��һҳ':
            f.seek(-200,1)
            '''
            if f.tell()<208 and f.tell()>100:
                f.seek(0,0)
                print f.read(100)
            elif f.tell() == 208:
                print '�Ѿ��ǵ�һҳ'
            '''
            
            print f.read(100)    
        elif b == '��һҳ':
            f.seek(0,1)
            print f.read(100)
            
f.close()
