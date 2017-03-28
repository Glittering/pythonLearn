#coding:gbk

      #声明字符集，
#python 代码的执行，执行的顺序
#默认情况代码 自左向右，自上向下 执行

#print 'hello_world'
      #
'''
for i in range(10):
      print i
print i
'''
#赋值
      #赋值的对象,只能是变量
#在python里
      #python的语言是一种弱变量语言
      #弱变量
            #在python当中，变量即用即生成

#变量在python并没有被封装
      #变量的类型是由值决定的

#查看变量的类型
'''
func = 456
func = 'hello world'
#使用type查看对象, object
print type(func)
'''

#数字
      #数字的类型
            #整型数
                  #长整型数
                        #2147483647
                        #-2147483648

            #浮点型数
                  #浮点数

#内置的函数。
#int 整型数的内置函数
#float 浮点数的内置函数
#long 长整型数的内置函数


#数字运算
# + - * /
#// 整除
#%  取余
# ** 求幂

#math 数学计算模块
#import math

#访问 www.python.org  python官方网站


#字符串
#string
'''
#手动构建字符串
print 'hello world'
print"string"
#print''''''
#print"""asd"""

#字符串实质
      #格式化输出引号内的字符(单词,数字,特殊字符 $// +)
func = 123
print 'func'
#内置函数
#repr() 
#str() 

#字符串的特性
      #有序
      #可迭代
      #不可变

#切片，切分

abc = "helloTworld5"
print abc
print abc[0:4:1]  #不取 4   不取上限

print abc[0:5:1]
print abc[0:5:3]  #步长
print abc[0:5:100]

print abc[1:5:1]

print abc[::]    #有默认值
print abc[0:11:1]#默认值的具体参数
#【 默认从0号索引位开始取值  : 默认上限+1 默认不取上限所对应的索引上的值 :默认步长为1 默认取值的方向是 自左向右】

print abc[-1:-20:-1]

print abc[0:5:-1]
print abc[0::-1]
#切片的依据是 依靠索引(index)取值。

for num in abc:
      print num
print num

print type(num)
'''
#注意：在print 打印的时候,num 显示的是数字,但是实质是 string 字符串

#字符串里面的特殊字符
#print "qwe\nqwe\nqwe\n"
# \ 转义符  
      # \n 换行
      # \t table缩写 TAB 默认情况下 \t 是8位空格  注意 \t被侵占的问题

# % 占位符
      # %s  string    传递字符串
      # %d  整型数    传递整形数
      # %f  float     传递浮点数
'''
int1 = 456
int2  = 456.0
int3 = 456.0000000000
str1 = 'world'

print 'string %s' %str1
print 'string %s' %int1

print 'string %s' %int3
print 'string %f' %int3
print 'string %0.10f' %int3  # 0.    10保留的小数点后面的多少位

print 'string %d' %int3   #传递进入字符串的当中的肯定是 整型数

# %s %d %f  都通用的参数
print 'qwe%20s' %789
      # %后面 20所代表的意义 就是 789所占的(20个空格)长度
'''
#format
'''
print '{1}'.format(0,"hello","sorry","string")
      #1, ''.format
            #括号里的元素 可以多次使用,没有次数影响.
      #2, 注意 字符串里面元素的索引, 必须在 format() 有他的索引值 

print '{[name]} {[hello]}'.format({'hello':78,'name':45},{'name':456,'hello':789})
      #1, {[name]} 根据 键 来取值
            #{'name':456}   是一个字典, dict 
'''
#字符串的方法
      #帮助命令
            #help()
            #help(str.__add__)
            #help(str.capitalize)
            #help(str)

#增加
'''
string1 = "hello world"
print string1.center(20,"@")  #center  填充  居中以后向两边延伸
print string1.rjust(50,'1')   #rjust     right 右对齐
print string1.ljust(50,'2')   #ljust    左对齐
print string1.zfill(50)       # 在右对齐的基础上,以0进行填充
print 'hello \t world'.expandtabs()
#默认 参数值 为 8,只对\t敏感，修改\t的长度
'''
#删减
string1 = "\thAllo world    "
#string1.strip() #默认删除两边的空格,(包括\n \t)
#string1.strip("abc")#从两边同时开始删除,参数给的元素,
            #注意！ 一但有一个元素,删除不掉,则停止删除
#string1.rstrip()#自右 开始删除
#string1.lstrip()#自左 开始删除

#变形
'''
print string1.lower()  #将字符串内所有的英文字母,由大写转换为小写
print string1.upper()  #将字符串内所有的英文字母,由小写转换为大写

print string1.capitalize() #字符串首字母大写,其他字母小写
print string1.swapcase()  #将字符串内字母,大小写互换.
print string1.title()     #字符串内 单词！ 首字母大写
'''
#切分
#注意！返回值为列表
'''
string1 = "\nhAllo\n world    "
print string1.splitlines()      #只对 \n 敏感
print string1.splitlines(True)  #
print string1.split()   #默认切 \n
print string1.split('l',1) #两个默认参数。切谁，切几次.
print string1.rsplit('l',1) #从右开始切分
'''
#连接
#print '123'+'456'
#print '123'*2

#print string1.join('123')# 把S(变量) 添加到 (参数)的元素与元素之间
#iterable  可迭代对象  join 里面的参数必须是可迭代的。

#字符串的判断
            #isalnum 字符串是否完全由数字和字母组成
            #isalpha 字符串是否完全由字母组成
            #isdigit 字符串是否完全由数字组成    
            #islower 判断字符串当中的字母是否完全小写
            #isupper 判断字符串当中的自摸是否完全大写
            #isspace 判断字符串是否完全由空格（包括\t\n）组成
            #istitle 判断字符串是否满足title 格式
            #startswith 判断字符串是否以指定的字符开头
            #endswitch 判断字符串是否以指定的字符结尾
#对象  --> 字符串
# .    -->  链接
# 方法的名称  -->
#()   --- >  参数可能是 0-无限个. *args **kwagrs

#字符串的查找
'''
print string1.index("h")  #自左向右，h 第一次出现的位置 1号索引位
print string1.index("l",4,)
#print string1.index("R")
print string1.find("W")  #自左向右，h 第一次出现的位置 1号索引位，若参数不存在,则返回-1
print string1.count("l")   #count 计数, 返回你指定元素在string1中，出现的次数
'''
#字符串的替换
print string1.replace("l","H")

#字符串编码
      #ASCII
      # encode
      # decode
      # unicode
      # chr()
      # ord()
      
      
#查询 循环，遍历，迭代  三者的关系，和异同。
    

#小作业， 使用什么工具来获取。字符串的字符集？？
      # 获取的方法
      # 获取的途径















