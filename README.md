# pythonLearn

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
	abs() 绝对值
	cmp() 比较函数
	int() 将其他类型转换为int  包括string  两个参数，默认第二位是10进制
	str() 类似于int
	sum() 接受一个list 返回和。
	sqrt()平方根	math包中
	

定义函数 def name(arg):
	return null 可以简写成 return

import 引入库

定义可变参数	*args
     
-----------

## 2016-12-22





