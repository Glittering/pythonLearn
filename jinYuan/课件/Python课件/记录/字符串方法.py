#coding:gbk

      #�����ַ�����
#python �����ִ�У�ִ�е�˳��
#Ĭ��������� �������ң��������� ִ��

#print 'hello_world'
      #
'''
for i in range(10):
      print i
print i
'''
#��ֵ
      #��ֵ�Ķ���,ֻ���Ǳ���
#��python��
      #python��������һ������������
      #������
            #��python���У��������ü�����

#������python��û�б���װ
      #��������������ֵ������

#�鿴����������
'''
func = 456
func = 'hello world'
#ʹ��type�鿴����, object
print type(func)
'''

#����
      #���ֵ�����
            #������
                  #��������
                        #2147483647
                        #-2147483648

            #��������
                  #������

#���õĺ�����
#int �����������ú���
#float �����������ú���
#long �������������ú���


#��������
# + - * /
#// ����
#%  ȡ��
# ** ����

#math ��ѧ����ģ��
#import math

#���� www.python.org  python�ٷ���վ


#�ַ���
#string
'''
#�ֶ������ַ���
print 'hello world'
print"string"
#print''''''
#print"""asd"""

#�ַ���ʵ��
      #��ʽ����������ڵ��ַ�(����,����,�����ַ� $// +)
func = 123
print 'func'
#���ú���
#repr() 
#str() 

#�ַ���������
      #����
      #�ɵ���
      #���ɱ�

#��Ƭ���з�

abc = "helloTworld5"
print abc
print abc[0:4:1]  #��ȡ 4   ��ȡ����

print abc[0:5:1]
print abc[0:5:3]  #����
print abc[0:5:100]

print abc[1:5:1]

print abc[::]    #��Ĭ��ֵ
print abc[0:11:1]#Ĭ��ֵ�ľ������
#�� Ĭ�ϴ�0������λ��ʼȡֵ  : Ĭ������+1 Ĭ�ϲ�ȡ��������Ӧ�������ϵ�ֵ :Ĭ�ϲ���Ϊ1 Ĭ��ȡֵ�ķ����� �������ҡ�

print abc[-1:-20:-1]

print abc[0:5:-1]
print abc[0::-1]
#��Ƭ�������� ��������(index)ȡֵ��

for num in abc:
      print num
print num

print type(num)
'''
#ע�⣺��print ��ӡ��ʱ��,num ��ʾ��������,����ʵ���� string �ַ���

#�ַ�������������ַ�
#print "qwe\nqwe\nqwe\n"
# \ ת���  
      # \n ����
      # \t table��д TAB Ĭ������� \t ��8λ�ո�  ע�� \t����ռ������

# % ռλ��
      # %s  string    �����ַ���
      # %d  ������    ����������
      # %f  float     ���ݸ�����
'''
int1 = 456
int2  = 456.0
int3 = 456.0000000000
str1 = 'world'

print 'string %s' %str1
print 'string %s' %int1

print 'string %s' %int3
print 'string %f' %int3
print 'string %0.10f' %int3  # 0.    10������С�������Ķ���λ

print 'string %d' %int3   #���ݽ����ַ����ĵ��еĿ϶��� ������

# %s %d %f  ��ͨ�õĲ���
print 'qwe%20s' %789
      # %���� 20����������� ���� 789��ռ��(20���ո�)����
'''
#format
'''
print '{1}'.format(0,"hello","sorry","string")
      #1, ''.format
            #�������Ԫ�� ���Զ��ʹ��,û�д���Ӱ��.
      #2, ע�� �ַ�������Ԫ�ص�����, ������ format() ����������ֵ 

print '{[name]} {[hello]}'.format({'hello':78,'name':45},{'name':456,'hello':789})
      #1, {[name]} ���� �� ��ȡֵ
            #{'name':456}   ��һ���ֵ�, dict 
'''
#�ַ����ķ���
      #��������
            #help()
            #help(str.__add__)
            #help(str.capitalize)
            #help(str)

#����
'''
string1 = "hello world"
print string1.center(20,"@")  #center  ���  �����Ժ�����������
print string1.rjust(50,'1')   #rjust     right �Ҷ���
print string1.ljust(50,'2')   #ljust    �����
print string1.zfill(50)       # ���Ҷ���Ļ�����,��0�������
print 'hello \t world'.expandtabs()
#Ĭ�� ����ֵ Ϊ 8,ֻ��\t���У��޸�\t�ĳ���
'''
#ɾ��
string1 = "\thAllo world    "
#string1.strip() #Ĭ��ɾ�����ߵĿո�,(����\n \t)
#string1.strip("abc")#������ͬʱ��ʼɾ��,��������Ԫ��,
            #ע�⣡ һ����һ��Ԫ��,ɾ������,��ֹͣɾ��
#string1.rstrip()#���� ��ʼɾ��
#string1.lstrip()#���� ��ʼɾ��

#����
'''
print string1.lower()  #���ַ��������е�Ӣ����ĸ,�ɴ�дת��ΪСд
print string1.upper()  #���ַ��������е�Ӣ����ĸ,��Сдת��Ϊ��д

print string1.capitalize() #�ַ�������ĸ��д,������ĸСд
print string1.swapcase()  #���ַ�������ĸ,��Сд����.
print string1.title()     #�ַ����� ���ʣ� ����ĸ��д
'''
#�з�
#ע�⣡����ֵΪ�б�
'''
string1 = "\nhAllo\n world    "
print string1.splitlines()      #ֻ�� \n ����
print string1.splitlines(True)  #
print string1.split()   #Ĭ���� \n
print string1.split('l',1) #����Ĭ�ϲ�������˭���м���.
print string1.rsplit('l',1) #���ҿ�ʼ�з�
'''
#����
#print '123'+'456'
#print '123'*2

#print string1.join('123')# ��S(����) ��ӵ� (����)��Ԫ����Ԫ��֮��
#iterable  �ɵ�������  join ����Ĳ��������ǿɵ����ġ�

#�ַ������ж�
            #isalnum �ַ����Ƿ���ȫ�����ֺ���ĸ���
            #isalpha �ַ����Ƿ���ȫ����ĸ���
            #isdigit �ַ����Ƿ���ȫ���������    
            #islower �ж��ַ������е���ĸ�Ƿ���ȫСд
            #isupper �ж��ַ������е������Ƿ���ȫ��д
            #isspace �ж��ַ����Ƿ���ȫ�ɿո񣨰���\t\n�����
            #istitle �ж��ַ����Ƿ�����title ��ʽ
            #startswith �ж��ַ����Ƿ���ָ�����ַ���ͷ
            #endswitch �ж��ַ����Ƿ���ָ�����ַ���β
#����  --> �ַ���
# .    -->  ����
# ����������  -->
#()   --- >  ���������� 0-���޸�. *args **kwagrs

#�ַ����Ĳ���
'''
print string1.index("h")  #�������ң�h ��һ�γ��ֵ�λ�� 1������λ
print string1.index("l",4,)
#print string1.index("R")
print string1.find("W")  #�������ң�h ��һ�γ��ֵ�λ�� 1������λ��������������,�򷵻�-1
print string1.count("l")   #count ����, ������ָ��Ԫ����string1�У����ֵĴ���
'''
#�ַ������滻
print string1.replace("l","H")

#�ַ�������
      #ASCII
      # encode
      # decode
      # unicode
      # chr()
      # ord()
      
      
#��ѯ ѭ��������������  ���ߵĹ�ϵ������ͬ��
    

#С��ҵ�� ʹ��ʲô��������ȡ���ַ������ַ�������
      # ��ȡ�ķ���
      # ��ȡ��;��















