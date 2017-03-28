#coding:gbk


#python 是一门弱变量语言，变量的类型由值的类型决定，变量即用即生成

#python 列表
    #list()
    #[]
    #range()
    #列表的方法
        #列表的添加
            #append 在指定列表的末尾追加一个元素
'''
l = range(10)
l.append(100)
l.append('abc')
#print l
'''
            #extend 将可迭代对象拆分，依次添加到指定列表当中
'''
l = range(10)
l.append('abc')
l.extend('abc')
l.extend(['1','2','3'])
print l
'''
            #insert 在指定的索引位之前插入指定的元素
'''
l = range(10)
#print l
l.insert(3,'name')
print l
l.insert(6,'age')
print l
'''
        #列表的查找
            #count 在指定的列表当中，查找指定元素出现的次数
l = [1,25,2,65,2,44,25,15,25,2,25]
#print l.count(20)
            #index 在指定的列表当中查找指定的元素，如果存在，返回第一次出现的索引位
                   #如果不存在，报错
#print l.index(25)
#print l.index(25,3,7)

        #列表的删除
            #remove 在指定的列表当中，删除指定的元素
l = ['a',1,'b','a',2,'c',3]
#print l.remove('a')
#print l
            #pop 默认弹出最后一个索引位上的元素
#print l.pop()
'''
print l.pop(3)  #弹出指定索引位上的元素
print l
'''

        #列表的排序
            #sort  正排序
l = ['a','*',14,'R',35,'w','@',25,',','c','%','F','C']
#l.sort()
#print l
            #reverse 按索引倒排序
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

#公共的方法
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

#python 元组  因为元组的不可修改性，一般用元组写配置文件
    #定义
        #()
        #tuple()
        #单元素元组必须以逗号结尾
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

    #元组的方法
        #count 在指定的元组当中，查找指定元素出现的次数
t = (2,3,'a','b','c','d','a',1,'2','a')
#print t.count('a')
        #index 在指定的元组当中查找指定元素，如果存在，返回第一次出现的索引位
               #如果不存在，报错
'''
print t.index('a',3,7)
print t.index('o')
'''


#python 字典：唯一一种映射关系的数据类型
    #字典的定义
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
            #zip 将序列相同索引位上的元素合并到一个元组当中，并返回列表形式,以短序列为主

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
    #字典的访问
        #以键取值
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
    #字典的方法
        #get  在指定的字典当中获取指定键所对应的值，如果键存在，返回键所对应的值
              #如果键不存在，返回设置的默认值，没有默认值，返回None

#print d.get('age')
#print d.get('aaa')
#print d.get('aaa','hello world')
#print d.get('name','xiaoqiang')
#print d

        #setdefault 设置默认值，如果键存在返回键所对应的值。
                    #如果键不存在，向字典中添加一个元素
'''
#print d.setdefault('name')
print d.setdefault('aaa')
print d.setdefault('address','HaiNan')
print d
'''
d = {'name':'laoli','age':30,'gender':'nan'}

        #keys 获取指定字典的键
#print d.keys()
        #values 获取指定字典的值
#print d.values()
        #items 将字典的键和值合并到一个元组当中，并返回列表形式
#print d.items()

        #pop 弹出指定的键值对
'''
print d.pop('age')
print d.pop('aaa','hello')
#print d.pop('aaa')
print d
'''
        #popitem 随机弹出键值对
'''
print d.popitem()
print d
'''

        #update 更新
'''
d.update(name = 'xiaoqiang')
d.update(address = 'BeiJing',age = 20)
print d
'''
        #has_key 判断指定键是否在指定字典当中存在（python3不存在）
        #in
d = dict(zip('abcd',range(5)))
'''
print d.has_key('c')
print d.has_key('a')     
print d.has_key('f')
'''
#print 'a' in d
#print 'q' in d


        #视图模式
            #viewkeys
#print d.viewkeys()
            #viewvalus
#print d.viewvalues()
            #viewitems
#print d.viewitems()

        #迭代模式
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
        #clear 清空字典,保留字典队象
'''
d = dict(zip('abc',[1,2,3]))
print d
d.clear()
print d

del d
print d
'''

