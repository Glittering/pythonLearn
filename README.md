# pythonLearn


#python 基础课

## 2016-12-21

e在浮点数中表示10的多少次方

python中字符串可以用''或者""不再跟java中一样区分字符和串

布尔值 True False 大小写注意
	and or not 是与或非运算

None 表示空 类比null

注释和C一样用#

变量类型不固定，是动态语言。
	变量不需要声明变量类型

raw 用r 表示不转义 单行用'' 多行用'''...'''

中文用 Unicode u''

0 空字符串'' 和 None 看成是 False
其他数值，非空字符串 看成是 True

list 用[]
	List中的-1下标表示最后一个  -2 -3
	List 添加元素。append  insert
	     删除元素  pop()	空表示最后一个。数字为删除位置下标

tuple	用 () 元组。 创建即固定不能修改		读取时用的还是[]
	()有歧义，可以表示运算级。所以单元素元组需要加上一个，
	
python 用缩进来表示代码块。	4个空格表示缩进。不要用tab

if 条件 :
	代码块


if 条件 ：
	代码块
else ：


else if 在python中为 elif


for 迭代  for name in L：

用 + 做连接符，没有空格。
用 ，做连接符，有空格。

dict	字典类型
	键值对 key：value
	len（） 可以求d的长度
	取值  d['Adam']
	      d.get('Adam')
	修改和添加都是 d[key] = 'value'
	for key in d	遍历
	pop() 删除


集合中包含某元素用 in

set 没有重复，而且无序。
	创建方式是调用set()并传入一个list。
	用来判断某元素是否存在
	更新set。add()添加。remove()移除元素   ()里写的是元素内容而不是下标
	add() 里只可以是元素 
	
内置函数
+	abs() 绝对值
+	cmp() 比较函数
+	int() 将其他类型转换为int  包括string  两个参数，默认第二位是10进制
+	str() 类似于int
+	sum() 接受一个list 返回和。
+	sqrt()平方根	math包中
+	range(1, 101) 创建1到100数列
+	string.upper() 字符变大写
+	enumerate() 给有序集合绑定索引1
+	zip() 把两个list变成一个list
+	dict.values() 把dict转换成一个包含所有value的list
-		itervalues()
+	dict.items() 返回一个包含tuple的list
-		iteritems()
+	join() 可以将一个list拼接成字符串
+ 	isinstance(x, str) 可以判断是否字符串


定义函数 def name(arg):
	return null 可以简写成 return

import 引入库

定义可变参数	*args
     
-----------

## 2016-12-23

Slice 切片 [0:3] 取0-3,不包括3 0可以省略
	L[:] 表示从头到尾，复制出了一个新List
	L[::n] 每N个取一个

range(1, 101) 创建1到100数列

string.upper() 把字符变成大写字母

集合按照有序无序分类
+ 有序集合：list, tuple, str, unicode
+ 无序集合：set
+ 无序集合并且有键值对：dict

Python中 迭代**永远取元素本身**，而非元素的索引

enumerate() 给有序集合绑定索引

zip() 把两个list变成一个list

dict.values() 把dict转换成一个包含所有value的list
	itervalues() 类似
+ values() 创建一个list
+ itervalues() 不会转换，节省内存
+ itervalues 返回的是一个键值对

dict.items() 返回一个包含tuple的list
	iteritems()

列表生成式 [x * x for x in range(1, 11)]

['111%s2222%s' % (n, s) for n, s in d.iteritems()]

join() 可以将一个list拼接成字符串

列表生成式的 for **循环后面还可以加上 if 判断**
	[x * x for x in range(1, 11) if x % 2 == 0]

isinstance(x, str) 可以判断是否字符串

列表生成式可以用多层循环嵌套



#python 进阶课

##2016-12-23

为什么用高阶函数，而不是直接调用这个函数呢？？？

##2016-12-25

map() 接收一个**函数** f 和一个 list，把函数 f 依次作用在 list 的每个元素上
	2_2_4.py

reduce() 一个函数 f，一个list, f 必须接收两个参数,可以接收第3个可选参数，作为计算的初始值。
	2_2_5.py

filter() 接收一个函数 f 和一个list对每个元素进行判断，返回 True或 False.根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
	2_2_6.py

s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')

sorted() 接受list，对其排序。
	接受list 和 函数 x 则按照函数排序
	2_2_7.py

.返回函数	
	2_2_8.py

##2016-12-26

闭包 要确保**局部变量不变**
	2_2_9.py



##2016-12-30

+ 通配符 .

+ 通配符转义 \\.

+ 字符集[ ] ‘[a-zA-Z0-9]’能够匹配任意大小写字母和数字 反转字符集 [^abc]

+ 选择符 | 或的意思

+ 子模式 p(ython | erl) 

+ 可选项 子模式后面加上问号 r’(heep://)?(www\.)?python\.org’	只能匹配下列字符：‘http://www.python.org’	‘http://python.org’	‘www.python.org’	‘python.org’

+ 重复子模式 (pattern)* : 允许模式重复0次或多次	(pattern)+ : 允许模式重复1次或多次	(pattern){m,n} : 允许模式重复m~ n 次


lambda 匿名函数，
	2_2_10.py

装饰器	@相当于调用函数再赋值给它本身
+ @log 打印日志
+ @performance 检测性能
+ @transaction 数据库事务
+ @post('/register') URL路由
	f=decorate(f) 装饰器的定义

重新定义log 使参数自适应
def log(f):
    def fn(*args, **kw):
        print 'call ' + f.__name__ + '()...'
    return f(*args, **kw)
return fn
	2_2_12.py 2_2_13.py

@functools.wraps(f) 把原函数的所有必要属性都一个一个复制到新函数上 import functools
	2_2_14.py

functools.partial 把一个参数多的函数变成一个参数少的新函数 int2 = functools.partial(int, base=2) import functools
	2_2_15.py

##2017-1-1

模块，直接用.py文件夹

包中必须含有__init__.py 来表示目录

pow math中。 表示次方

只希望导入用到的math模块的某几个函数 from math import pow, sin, log
 from math log as logInMath

os.path模块提供了 isdir() 和 isfile()函数  判断指定的目录和文件是否存在
	2_3_2.py

利用ImportError错误 i动态导入模块
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
	2_3_3.py

在Python 2.7中引入3.x的规则，导入__future__
	2_3_4.py

2.7中 整数除法结果是整数  3之后是浮点数
	默认字符串是字节 汉字等加u 3之后默认unicode 字节存储加b

初始化类  用的 def __init__(): 这个方法

创建类 	
	2_4_2.py

创建实例属性
	2_4_3.py

初始化实例属性 添加一个特殊的__init__()方法 第一个参数必须是 self
	2_4_4.py

隐藏属性：在属性前加上__
	2_4_5.py


类的属性  对象继承并新建了另一个属性
	2_4_6.py

del 可以删除 对象的属性	例如删除对象的同名属性以显示类的属性
	2_4_7.py

隐藏数据
	2_4_8.py

python 中的方法也是属性
	2_4_9.py

@classmethod，该方法将绑定到 Person 类上，而非类的实例 参数名命名为 cls
	2_4_10.py

##2017-1-2

继承 在继承的类中init里要写 super(类名, self).__init__(变量表) 
	2_5_2.py

isinstance() 判断变量类型，可以用内置数据类型 str list dict ，或者自己定义的类
	2_5_3.py	继承后类型的判定

python的多态因为是动态的，所以不检测类型。
json.load() 把文件或者任何对象 File-like Object 当作json类型读取。
	2_5_4.py

多重继承的公共方法，只被调用一次。
	2_5_5.py

type() 函数获取变量的类型，它返回一个 Type 对象

dir() 函数获取变量的所有属性

获取或者设置对象的属性，就需要用 getattr() 和 setattr( )函数
	getattr(s, 'name')  # 获取name属性
	setattr(s, 'name', 'Adam')  # 设置新的name属性
	2_5_6.py

##2016-1-3

__str__和__repr__方法 print 默认调用
	2_6_2.py

__cmp__ 默认sorted调用
	2_6_3.py

__len__() 返回元素的个数
	2_6_4.py

ational类来表示有理数
	2_6_5.py

__int__(): __float__()。
	2_6_6.py

score(self)是get方法，用@property装饰	
score(self, score)是set方法，用@score.setter装饰
	只有第一个时是只读方法
	2_6_7.py

__slots__ 限制添加的属性
 __slots__ = ('name', 'gender', 'score')
	2_6_8.py

一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()。
	2_6_9.py


##2017年 03月 13日 星期一 08:53:58 CST

1. replace 可以将第一个字符串用第二个替代

2. python的比较可以多级并联    -3&lt;-2&lt;-1   *True*

3. True的数值相当于1

4. 浮点和整数可以比较

5. in 成员运算符： 测试前者是否存在于后面的**集合**中

6. is 身份运算符： 归属关系。
	身份  类型  值 都相同

7. 布尔运算符： not  and  or

8. range(1,11) 生成1-10

9. 格式化输出
    print ('%d'%(2))
    print ('{}'.format(2))
    print ('{1},{2}'.format(1,2))
    print ('{tab},{label}'.format('tab'=2;'label'=1))

10. print 在py3中可以用 print(content,end='') 以''中的内容结尾
    py2中 只能用 sys.stdout.write() 来输出但不换行

11. sum() 可以直接对list求和

12. sorted(list)
    sorted(list,reverse=True) 逆序
    
13. ipython python的终端


#2017年 03月 14日 星期二 08:50:38 CST

1. string.punctuation 所有符号
    和split一同使用可以切分字符串
    和strip一同使用删除所有包含标点

2. 可以用转换成set来去除重复元素

3. lambda生成简单函数 

4. with ... as ... 打开文件，并传参。 安全做法，自动关闭。


