#!D:\Python27\python.exe 
#coding:gbk
#! usr/bin/env python


#�ҵĵ��� --> �һ� --> ���� --> �߼�ϵͳ���� --> ��������

#print 100 * 100
#print(100*100)
#ע��
    #����ע�� #
    #����ע�� 
        #�������� ''' '''
        #��˫���� """ """

#.py �ű��ļ�
#.pyc ��ʱ�ļ�
#.pyw ͼ�λ��ļ�

#����ģ�� Lib
#����ģ�� Lib\site-packages
    #ѹ��������ѹ����CMD���л�Ŀ¼���е���ѹĿ¼֮���ҵ�setup.py��Ȼ��ִ��python setup.py install
    #.exe 

#��дģ�� 
#import hello
import time

#dir() �鿴ָ�����������
#help() �鿴���Եľ����÷�



#python ��������
    #������ int
    #�������� long
    #������ float
    #���������
        #+ - * / % **  //�ذ��

#len�鿴ָ������ĳ���

#python ��������
    #int
    #long
    #float
    #�ַ��� str:�����Ű�Χ�ģ�Ԫ�ؿ������������͵�,����ġ������޸ĵ�����
        #�ַ����Ķ���
            #str
            #''
            #" "
            #''' '''   """ """  ֧�ֻ���
        #�����ַ�
            #\n ���з�
            #\t ˮƽ�Ʊ��
            #\v ��ֱ�Ʊ��
        #ռλ��
            #%s 
            #%d ����������
            #%f ���ݸ����� '%0.3f'
'''
>>> 'a%10sb'%'hello'
'a     hellob'
>>> '%10d'%123
'       123'
>>> '%-10d'%123
'123       '
'''


        #�ַ����ĸ�ʽ��
            # % ��ʽ����
            #format
'''
>>> 'name:%s,age:%d'%('xiaoli',20)
'name:xiaoli,age:20'

>>> 'name:{0},age:{1}'.format('xiaoli',20)
'name:xiaoli,age:20'
>>> 'name:{1},age:{0}'.format('xiaoli',20)
'name:20,age:xiaoli'
'''

#name = 'laoli'  �����ں��ұߵ�ֵ��ֵ����ߵı���

'''
>>> name = 'laozhang'
>>> age = 30
>>> 'name:{0},age:{1}'.format(name,age)
'name:laozhang,age:30'
>>> 'name:%s,age:%d'%(name,age)
'name:laozhang,age:30'
'''
        #ת���
            #\
            #% ֻת������

'''
>>> '%d%'%10

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    '%d%'%10
ValueError: incomplete format
>>> '%d%%'%10
'10%'
>>> '%d\%'%10

Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    '%d\%'%10
ValueError: incomplete format
'''
        #�ַ����ķ�Ƭ����(��������)
s = 'hello python'
#print s[0]
#print s[4]
#print s[10]
#print s[-2]
'''
print s[1:10]  #�����ޣ�������
print s[4:9]
'''
#print s[4:]
#print s[:10]
#print s[1:10]
#print s[1:10:2]  #����Ϊ2
#print s[1:10:3]
#print s
#print s[::]
#print s[::2]
#print s[::-1]
#print s[1:10:-1]
'''
print s[::-2]
print s[1:10:-2]
'''
        #�ַ����ı��� --> ��ĸ

            #upper ��Сд��ĸת��Ϊ��д��ĸ
s = 'Hello World'
#print s.upper()
#print s
            #lower ����д��ĸת��ΪСд��ĸ
#print s.lower()

            #title �������ַ���д
#print 'hi,I am xiaozhen'.title()

            #capitalize �ַ������ַ���д
#print 'Hi,I am Xiaozhen'.capitalize()

            #swapcase ��Сд����
#print s.swapcase()

#print '[123abc,'.upper()

        #�ַ��������
            #center ��ָ�����ַ������Ͼ��У�����ĵط�Ĭ���Կհ׷����
'''
s = '12345'
print s.center(15)
'''
            #ljust  ��ָ�����ַ������������
s = 'hello'
'''
print s.ljust(15)
print s.ljust(15,'*')
'''
            #rjust  ��ָ�����ַ��������Ҷ���
#print s.rjust(15)
#print s.rjust(15,'0')

            #zfill ��ָ�����ַ��������Ҷ��룬Ĭ����0���
#print s.zfill(15)

#range(10)
            #expandtabs
                #\t Ĭ��Ϊ8���ַ�����
'''
print 'a\tb'
print 'a\tb'.expandtabs(15)
'''
        #�ַ�����ɾ��
            #strip  Ĭ��ɾ���ַ������˵Ŀհ׷�
s = '   hello world       '
#print s
#print s.strip()
a = 'hellohh'
#print a.strip('h')
#print a

            #lstrip Ĭ��ɾ���ַ�����ߵĿհ׷�
#print s.lstrip()
#print a.lstrip('h')

            #rstrip Ĭ��ɾ���ַ����ұߵĿհ׷�
#print s.rstrip()



        #�ַ������з�
            #split Ĭ���Կհ׷��������з�ָ�����ַ���
s = "My name is xiaoqiang,my job is ITmonkey!!!"
#print s.split()
#print s.split('o')
#print s.split('o',2) #��ָ�����ַ��Թ涨�Ĵ����з��ַ���

            #rsplit Ĭ���Կհ׷����ҵ����з�ָ�����ַ���
#print s.rsplit('o',2)


        #�ַ�����ƴ��
            #join ���ɵ��������֣�ѭ�����

a = 'hello'
b = 'abc'
#print a.join(b)

            # + ƴ��
#print a + b

            # * �ظ�
#print 'abc' * 10
            

        #�ַ����Ĳ���
            #find ��ָ�����ַ������У������Ҳ���ָ�����ַ���������ڣ����ص�һ�γ��ֵ�����λ
                  #��������ڣ�����-1
            #rfind
s = "My name is xiaoqiang,my job is ITmonkey!!!"
#print s.find('o')
#print s[14]
#print s.find('o',15)
'''
print s.find('o',15,25)
print s.find('o',14,26)
'''
#print s.rfind('o')

            #index ��ָ�����ַ������У������Ҳ���ָ�����ַ���������ڣ����ص�һ�γ��ֵ�����λ
                   #��������ڣ�����
#print s.index('o')
#print s.index('o',15,25)

            #rindex

            #count ��ָ�����ַ������в���ָ���ַ����ֵĴ���
#print s.count('o')
#print s.count('o',15)
#print s.count('o',15,25)
            
           

        #�ַ������ж�
            #isalnum �ж�ָ���ַ����Ƿ���ȫ�����ֻ���ĸ���
s = 'hello:123'
#print s.isalnum()
            #isalpha �ж�ָ���ַ����Ƿ���ȫ����ĸ���
'''
print s.isalpha()
print 'ABCabc'.isalpha()
'''
            #isdigit �ж�ָ���ַ����Ƿ���ȫ���������
#print '12345'.isdigit()

            #isspace �ж�ָ���ַ����Ƿ���ȫ�ɿհ׷����
#print '123 abc'.isspace()
#print '   '.isspace()


            #isupper �ж�ָ���ַ����Ƿ���ȫ�д�д��ĸ���
s = 'Hello wolrd'
#print s.isupper()
#print 'ABC'.isupper()

            #islower �ж�ָ���ַ����Ƿ���ȫ��Сд��ĸ���
#print 'abc'.islower()

            #istitle �ж��Ƿ����title
#print s.istitle()


            #startswith �ж�ָ���ַ����Ƿ���ָ���ַ���ͷ
'''
#print 'My name is xiaoli.'.startswith('a')
print 'My name is xiaoli.'.startswith('My name')
'''
#print 'My name is xiaoli.'.startswith('a',4,10)

            #endswith  �ж�ָ���ַ����Ƿ���ָ���ַ���β
#print 'My name is xiaoli.'.endswith('li.')
#print 'My name is xiaoli.'.endswith('xiao',7,15)


        #�ַ����ı���
            #encode ����
            #decode ����
#print '����'.encode('utf-8')
#print '����'.decode('gbk')
#GB2312
#cp936
#unicode


        #�ַ������滻
            #replace ��ԭ���ַ��滻Ϊָ�����ַ������Թ涨�滻�Ĵ���
s = 'hello world'
#print s.replace('l','*')
#print s.replace('ll','*',2)




    #�б� list:�������Ű�Χ�ģ�Ԫ�ؿ������������͵ģ�Ԫ��֮���Զ��Ÿ����ģ�����ġ����޸ĵ�����
        #�б�Ķ���
            #list()
            #[]
            #range()

'''
>>> list('123')
['1', '2', '3']
>>> list((123,456,'abc'))
[123, 456, 'abc']
>>> [1,2,3]
[1, 2, 3]
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(5)
[0, 1, 2, 3, 4]
>>> range(11)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1,11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(1,11,2)
[1, 3, 5, 7, 9]
>>> range(1,11,3)
[1, 4, 7, 10]
'''
#xrange
'''
>>> l = range(10)
>>> type(l)
<type 'list'>
>>> a = xrange(10)
>>> type(a)
<type 'xrange'>
'''
        #�б������
l = range(1,11)
#print l[0]
#print l[1:5]
#print l[::2]
#print l[::-1]
l = ['name',['age',['gender',['address',100]]]]
#print len(l)
'''
a = l[1]
b = a[1]
c = b[1]
print c[1]
'''
#print l[1][1][1][-1]


    #Ԫ�� tuple:��С���Ű�Χ�ģ�Ԫ�ؿ������������͵ģ�Ԫ��֮���Զ��Ÿ����ģ�����ġ������޸ĵ�����
    #�ֵ� dict���Դ����Ű�Χ�ģ�Ԫ�سʼ�ֵ����ʾ�ģ�Ԫ��֮���Զ��Ÿ����ģ�����ġ����޸ĵ�����
    #�ֽ� bytes

'''
�������Ű�Χ�ģ�
Ԫ�ؿ������������͵ģ�
Ԫ��֮���Զ��Ÿ����ģ�
����ġ����޸ĵ����С�
'''



