#coding:gbk


#python ��һ�����������ԣ�������������ֵ�����;������������ü�����

#python �б�
    #list()
    #[]
    #range()
    #�б�ķ���
        #�б�����
            #append ��ָ���б��ĩβ׷��һ��Ԫ��
'''
l = range(10)
l.append(100)
l.append('abc')
#print l
'''
            #extend ���ɵ��������֣�������ӵ�ָ���б���
'''
l = range(10)
l.append('abc')
l.extend('abc')
l.extend(['1','2','3'])
print l
'''
            #insert ��ָ��������λ֮ǰ����ָ����Ԫ��
'''
l = range(10)
#print l
l.insert(3,'name')
print l
l.insert(6,'age')
print l
'''
        #�б�Ĳ���
            #count ��ָ�����б��У�����ָ��Ԫ�س��ֵĴ���
l = [1,25,2,65,2,44,25,15,25,2,25]
#print l.count(20)
            #index ��ָ�����б��в���ָ����Ԫ�أ�������ڣ����ص�һ�γ��ֵ�����λ
                   #��������ڣ�����
#print l.index(25)
#print l.index(25,3,7)

        #�б��ɾ��
            #remove ��ָ�����б��У�ɾ��ָ����Ԫ��
l = ['a',1,'b','a',2,'c',3]
#print l.remove('a')
#print l
            #pop Ĭ�ϵ������һ������λ�ϵ�Ԫ��
#print l.pop()
'''
print l.pop(3)  #����ָ������λ�ϵ�Ԫ��
print l
'''

        #�б������
            #sort  ������
l = ['a','*',14,'R',35,'w','@',25,',','c','%','F','C']
#l.sort()
#print l
            #reverse ������������
#l.reverse()
#print l
'''
l.sort()
l.reverse()
'''
'''
l.sort(reverse = True)
print l
'''


#sorted
#print sorted(l)
#print l

#reversed
'''
i = reversed(l)
print dir(i)
print i.next()
'''
#set
l = [1,25,2,65,2,44,25,15,25,2,25]
a = [1,3,5,7,9]
b = [2,4,1,3,6,8]

#print set(l)
#print set(a)|set(b)
#print set(a)&set(b)

#�����ķ���
    #del
'''
del l[3]
print l
'''
'''
del l
print l
'''
'''
s = 'hello world'
#del s[4]
del s
print s
'''

#python Ԫ��  ��ΪԪ��Ĳ����޸��ԣ�һ����Ԫ��д�����ļ�
    #����
        #()
        #tuple()
        #��Ԫ��Ԫ������Զ��Ž�β
'''
>>> a = ([1,2,3])
>>> a
[1, 2, 3]
>>> (1)
1
>>> ('name')
'name'
>>> (1,)
(1,)
>>> ('name',)
('name',)
>>> ([1,2,3],)
([1, 2, 3],)
'''
t = tuple(range(2,10))
'''
print t[6]
print t[2:6]
print t[::-1]
print t[::2]
'''

    #Ԫ��ķ���
        #count ��ָ����Ԫ�鵱�У�����ָ��Ԫ�س��ֵĴ���
t = (2,3,'a','b','c','d','a',1,'2','a')
#print t.count('a')
        #index ��ָ����Ԫ�鵱�в���ָ��Ԫ�أ�������ڣ����ص�һ�γ��ֵ�����λ
               #��������ڣ�����
'''
print t.index('a',3,7)
print t.index('o')
'''


#python �ֵ䣺Ψһһ��ӳ���ϵ����������
    #�ֵ�Ķ���
        #{}
        #dict()
'''
>>> dict([['a',1]])
{'a': 1}
>>> dict([['a',1],['age',30]])
{'a': 1, 'age': 30}
>>> dict([('a',1),('age',30)])
{'a': 1, 'age': 30}

>>> dict((('name','xiaozhang'),))
{'name': 'xiaozhang'}
>>> dict((('name','xiaozhang'),(10,10)))
{10: 10, 'name': 'xiaozhang'}

>>> dict((['name','xiaozhang'],[10,10]))
{10: 10, 'name': 'xiaozhang'}
'''
        #dict(zip())
            #zip ��������ͬ����λ�ϵ�Ԫ�غϲ���һ��Ԫ�鵱�У��������б���ʽ,�Զ�����Ϊ��

'''
>>> zip('abcd')
[('a',), ('b',), ('c',), ('d',)]
>>> zip('abcdefg',range(10))
[('a', 0), ('b', 1), ('c', 2), ('d', 3), ('e', 4), ('f', 5), ('g', 6)]
>>> zip('abcdefg',range(5),('A','B','C'))
[('a', 0, 'A'), ('b', 1, 'B'), ('c', 2, 'C')]
'''

'''
>>> dict(zip('abcd',range(5)))
{'a': 0, 'c': 2, 'b': 1, 'd': 3}
'''
    #�ֵ�ķ���
        #�Լ�ȡֵ
d = {'name':'laoli','age':30,'gender':'nan'}
#print d
#print d['name']
#print d['gender']
#print d['address']
#d['name'] = 'xiaoqiang'
#d['address'] = 'BeiJing'
#print d
'''
del d['gender']
print d
'''
    #�ֵ�ķ���
        #get  ��ָ�����ֵ䵱�л�ȡָ��������Ӧ��ֵ����������ڣ����ؼ�����Ӧ��ֵ
              #����������ڣ��������õ�Ĭ��ֵ��û��Ĭ��ֵ������None

#print d.get('age')
#print d.get('aaa')
#print d.get('aaa','hello world')
#print d.get('name','xiaoqiang')
#print d

        #setdefault ����Ĭ��ֵ����������ڷ��ؼ�����Ӧ��ֵ��
                    #����������ڣ����ֵ������һ��Ԫ��
'''
#print d.setdefault('name')
print d.setdefault('aaa')
print d.setdefault('address','HaiNan')
print d
'''
d = {'name':'laoli','age':30,'gender':'nan'}

        #keys ��ȡָ���ֵ�ļ�
#print d.keys()
        #values ��ȡָ���ֵ��ֵ
#print d.values()
        #items ���ֵ�ļ���ֵ�ϲ���һ��Ԫ�鵱�У��������б���ʽ
#print d.items()

        #pop ����ָ���ļ�ֵ��
'''
print d.pop('age')
print d.pop('aaa','hello')
#print d.pop('aaa')
print d
'''
        #popitem ���������ֵ��
'''
print d.popitem()
print d
'''

        #update ����
'''
d.update(name = 'xiaoqiang')
d.update(address = 'BeiJing',age = 20)
print d
'''
        #has_key �ж�ָ�����Ƿ���ָ���ֵ䵱�д��ڣ�python3�����ڣ�
        #in
d = dict(zip('abcd',range(5)))
'''
print d.has_key('c')
print d.has_key('a')     
print d.has_key('f')
'''
#print 'a' in d
#print 'q' in d


        #��ͼģʽ
            #viewkeys
#print d.viewkeys()
            #viewvalus
#print d.viewvalues()
            #viewitems
#print d.viewitems()

        #����ģʽ
            #iterkeys
#print d.iterkeys()
            #itervalues
#print d.itervalues()
            #iteritems
#print d.iteritems()

a = d.iteritems()
#print a.next()
'''
for i in d.iteritems():
    print i

print '\n'
for j in d.items():
    print j
'''
'''
for i in d.keys():
    print i

for i in d.iterkeys():
    print i
'''
        #clear ����ֵ�,�����ֵ����
'''
d = dict(zip('abc',[1,2,3]))
print d
d.clear()
print d

del d
print d
'''

