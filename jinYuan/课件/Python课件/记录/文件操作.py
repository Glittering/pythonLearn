#coding:gbk

import time

#print time.strftime('%Y-%m-%d %H:%M:%S') #��struct_timeʱ�䰴�ո�ʽ���ַ������
#print time.strftime('%I:%M:%S %p')
#print time.strftime('%A %B')
#print time.strftime('%a %b')
#print time.strftime('%Y-%m-%d %H:%M:%S',(2017,1,1,12,12,12,0,0,0))


'''
thetime = raw_input('Please Enter:')
#print thetime
now = time.time()
y,m,d = thetime.split('-')
tm = time.mktime((int(y),int(m),int(d),0,0,0,0,0,0))
print int((now - tm)/3600/24)
'''
'''
def thetime(y,m,d):
    now = time.time()
    tm = time.mktime((y,m,d,0,0,0,0,0,0))
    result = int((now - tm) / 3600 / 24)
    print result

if __name__ == '__main__':
    theday = raw_input('Please Enter:')
    a = theday.split(theday[4])
    #y = int(a[0])
    #m = int(a[1])
    #d = int(a[2])
    y,m,d = [int(i) for i in a]
    thetime(y,m,d)
    
'''

#python �ļ�����
'''
reportlab
xlrd xlwt
logging
PIL
tarfile
zipfile
'''
    #1�������ļ���������
        #open or file
            #path �ļ�·��
            #mode Ȩ��
                #r   ��
                #w   ����д
                #a   ׷��д
                #rb  �Զ����ƵĶ�
                #wb  �Զ����Ƶ�д
                #Ua  ͨ�û��з���д
                #rU  ���û��з��Ķ�
                #r+ w+ a+ ��д˫ģʽ
'''
f1 = open('django.txt','r')
print dir(f1)

print '\n'

f2 = file('django.txt','r')
print dir(f2)
'''

    #2���ļ�����
        #��
            #read  ��ȫ��
            #redaline  ��һ��
            #readlines ���ж�ȫ�ģ������б���ʽ��ÿһ�����б��һ��Ԫ�أ�

        #д
            #write  д�ַ���
            #writelines  д����

        #ָ��
            #seek
                #��һ��������ָ���ƶ�����Ծ���
                #�ڶ�������
                    #0 �ӿ�ͷ
                    #1 �ӵ�ǰ
                    #2 ��ĩβ

            #tell ����ָ���λ��

    #3���ر��ļ���������
        #close
'''
f = open('C:\Users\guozheng\Desktop\chat\django.txt','r')
#print help(f.read)
print f.read(100)
f.close()
'''
'''
f = open('django.txt','r')
#print f.readline(15)
#print f.read(100)
print f.readline(100)
#print f.readline()
#print f.readline()
f.close()
'''
'''
f = open('1.txt','r')
#print f.readlines()
print f.read(10)
print 'hello world'
print f.read(15)
f.close()
'''
'''
f = open('1.txt','w')
#print help(f.write)
#f.write('hello world')
f.write('12345')
f.close()
'''
'''
name = 'xiaoqiang'
age = 20
f = open('2.txt','w')
#f.write('name:%s,age:%s'%(name,age))
f.write('hello')
f.write('12345')
f.close()
'''
'''
f = open('2.txt','w')
#f.writelines(['1','2','3'])
#f.write()
#f.writelines(('hello','123'))
f.write('[]')
f.close()
'''
'''
f = open('2.txt','a')
#f.write('hello')
f.write('123456')
f.close()
'''
'''
f = open('django.txt','r')
f.seek(14)
print f.read(15)
f.seek(20,1)
print f.read(32)
f.close()
'''
'''
f = open('django.txt','r')
f.seek(15,0)
print f.read(20)
f.seek(10,2)
print f.read()
f.close()
'''
'''
f = open('django.txt','r')
f.seek(0,2)
print f.tell()
f.close()
'''
'''
f = open('C:\Users\guozheng\Desktop\chat\\1.txt','r')
#f.seek(0,2)
#print f.tell()
print len(f.read())
f.close()
'''
#print len('�й�')
'''
f = open('hello.py','r')
f.seek(20)
print f.read(40)
print f.tell()
f.close()
'''
'''
f = open('2.txt','r')
print f.read(20)
f.seek(30,1)
print f.tell()
print f.read(40)
print f.tell()
f.close()
'''

