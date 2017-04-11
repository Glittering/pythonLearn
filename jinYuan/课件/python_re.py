#coding:gbk

import re

#python 正则（re）:是字符串的一种高级处理方式，通常用来进行匹配
    #内容匹配:通过描述所要匹配内容的特征进行匹配
        #匹配的规则
            #匹配内容的规则
                #原样匹配
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'
#print re.findall('is',s)

                # . 除了换行符之外的所有内容
#print re.findall('..',s)

                #\w 匹配所有的数字字母下划线
#print re.findall(r'\w',s)
#print re.findall(r'\w.',s)

                #\W 匹配所有非数字字母下划线的内容
#print re.findall(r'\W',s)
#print re.findall('\w\W',s)
                
                #\d 匹配所有的数字
#print re.findall(r'\d',s)
                #\D 匹配所有的非数字内容
#print re.findall(r'\D',s)
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'

#print re.findall(r'\w\d',s)
                
                #\s 匹配所有的空白符（包含\n、\t）
#print re.findall(r'\s',s)
                #\S 匹配所有的非空白符内容
#print re.findall(r'\S',s)

                #\b 单词边界，只匹配一个位置
#print re.findall(r'\b\w',s)
                #\B
#print re.findall(r'\w\B',s)              

                #\A 在字符串的开始位置进行匹配
#print re.findall(r'\A\w\w',s)
#print re.findall(r'\A\d',s)
                #\Z 在字符串的开始末尾进行匹配
#print re.findall(r'.\W\Z',s)

                #^ 在开头匹配
#print re.findall(r'^\w\w',s)

                #$ 在末尾匹配
#print re.findall(r'.\W$',s)
#print re.findall(r'^python$','python')

                #[] 匹配中括号里面任意一种
#print re.findall(r'[\W\d]',' , , ')
#print re.findall(r'[\W\d]',s)

                #[...-...] 匹配一个范围
                    #[a-z]  [A-Z] 
#print re.findall(r'[A-Z]',s)
#print re.findall(r'[0-9]',s)
#print re.findall(r'[h-w]',s)
#print re.findall(r'1[358]',s)
#print re.findall(r'[A-Za-z]',s)

                #[^...] 非
#print re.findall(r'[^\w]',s)
#print re.findall(r'\W',s)
#print re.findall(r'[^\D]',s)


                #() 组匹配，当组匹配出现的时候，其他的匹配做为组匹配的条件进行匹配，最终返回组匹配匹配到的内容
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'

#print re.findall(r'(\w)\d',s)
#print re.findall(r'\w\d',s)

                #(?P<name>...) 命名组
#print re.findall(r'(?P<xiaoli>\w)\d',s)

                #(?P=name) 调用命名组匹配到的结果
a = 'b2b c3e d4f g5g h6h o7i'
#print re.findall(r'(?P<xiaoli>\w)\d',a)
#print re.findall(r'(?P<xiaoli>\w)\d(?P=xiaoli)',a)
'''
b 2 b
c 3 c
d 4 d
g 5 g
h 6 h
o 7 o
'''
                #(.*) 贪婪匹配
#print re.findall(r'a(.*)b','abbbbbbbb')

                #(.*?) 反贪婪匹配
#print re.findall(r'a(.*?)b','abbbbbbbb')

html = '''
<html>
    <body>
        <p>hello <br/> world</p>
        <p style = 'color:red;'>123</p>
    </body>
</html>
'''
#print re.findall(r'<p>(.*?)</p>',html)
#print re.findall(r'<p .*>(.*?)</p>',html)

                #(?=...) 前瞻断言匹配
s = 'My name is xiao_zhen,\nI am 20 years old,\tmy job is ITmonkey!!!'

#print re.findall(r'\w(?=\d)',s)
#print re.findall(r'(\w)\d',s)
                #(?!...) 反前瞻断言匹配
#print re.findall(r'\w(?!\d)',s)
#print re.findall(r'(\w)\D',s)

                #(?<=...) 后顾断言匹配
#print re.findall(r'(?<=\d)\w',s)

                #(?<!...) 反后顾断言匹配

#print re.findall(r'(?<!\w)\d',s)

                #| 匹配管道符两边任意一边
#print re.findall(r'\W|\d',s)
#print re.findall(r'13|15|18')

            #匹配数量的规则
                #* 匹配0到多次
#print re.findall(r'\w*',s)
                #+ 匹配1到多次
#print re.findall(r'\w+',s)
                #? 匹配0到1次
#print re.findall(r'\w?',s)
                #{4} 匹配指定的次数
#print re.findall(r'\w{4}',s)
                #{2,4 }
#print re.findall(r'\w{2,4}',s)

            #特殊规则
z = 'AaBbAaCc'
                #re.I 忽略大小写
#print re.findall(r'a',z,re.I)

                #re.S 修改.的匹配方式
#print re.findall(r'.',s)
#print re.findall(r'.',s,re.S)

                #re.M 多行模式
s = '''My name is xiao_zhen,
I am 20 years old,
my job is ITmonkey!!!'''

#print re.findall(r'\A\w',s,re.M)
#print re.findall(r'^\w',s,re.M)

#print re.findall(r'.\Z',s,re.M)
#print re.findall(r'.$',s,re.M)

        #匹配的方法
            #findall 在指定字符串当中查找所有符合正则表达式描述的内容，并返回列表形式
#print re.findall(r'zzz',s)
s = '''My name is xiao_zhen,
I am 20 years old,
my job is ITmonkey!!!'''

            #search 在指定字符串当中查找符合正则表达式描述的内容，
                    #如果找到，返回匹配对象（第一次匹配到的内容）
                    #如果没有，返回None
#print re.search(r'\d',s)
#print re.search(r'zzz',s)

#匹配对象
    #group

    #gropus
m = re.search(r'\d',s)
#print m.group()
#print dir(m)
#print re.search(r'\w+',s).group()
#print re.search(r'\w+',s).groups()

            #match 在字符串的开头查找符合正则表达式描述的内容，
                    #如果找到，返回匹配对象（第一次匹配到的内容）
                    #如果没有，返回None
#print re.match(r'\w+',s).group()
#print re.match(r'\d+',s)
#print re.match(r'zzz',s)
#print re.match(r'\w+',s,re.M).group()

#print re.match(r'(\w)(.)',s).groups()
#print re.search(r'(\w+)(.)(\w+)',s).groups()
#print re.search(r'(\w+)(.)(\w+)',s).group()

            #compile 形成一个正则模板
p = re.compile(r'\w+')
#print dir(p)
#print p.findall(s)
#print re.findall(r'\w+',s)
#print re.findall(p,s)

            #sub 类似于字符串的replace方法
#print re.sub(r'\w','*',s)
#print s
#print re.sub(r'\w+','hello',s,3)

            #split 类似于字符串的split方法
#print re.split(r'\d',s)
#print re.split(r'\W',s,5)

    #结构匹配
        #lxml  BeautifulSoup
#print re.findall(r'\.','I am xiaoli.')


#匹配IP地址
#匹配身份证号
#匹配手机号


