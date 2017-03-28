#coding:gbk
import re

#python 正则表达式
    #re:一种字符串的高级处理方式，通常用于匹配
        #内容匹配:通过描述所要匹配内容的特点进行匹配
            #匹配的规则
                #匹配内容的规则
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."
                    #原样匹配
#print re.findall(r'm',s)

                    # . 匹配除了换行符之外的所有内容
#print re.findall(r'.',s)
#print re.findall(r'..',s)
#print re.findall(r'\.',s)
                    
                    #\s 匹配所有的空白符（包含\n,\t）
#print re.findall(r'\s',s)

                    #\S 匹配所有的非空白符内容
#print re.findall(r'\S',s)
                    
#print re.findall(r'\s.',s)

                    #\d 匹配所有的数字
#print re.findall(r'\d',s)
 
                    #\D 匹配所有非数字的内容
#print re.findall(r'\D',s)

#print re.findall(r'\d.',s)

                    #\w 匹配所有的数字字母下划线
#print re.findall(r'\w',s)
                    #\W 匹配所有的非数字字母下划线内容
#print re.findall(r'\W',s)

#print re.findall(r'\d\w',s)
                    
                    #\b 单词边界，只匹配一个位置
#print re.findall(r'\w\b',s)
#print re.findall(r'\b\w',s)
                    #\B 单词字母之间，只匹配一个位置
#print re.findall(r'\w\B',s)
#print re.findall(r'\B\w',s)
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."           
                    #\A 从字符串开头进行匹配
#print re.findall(r'\A\w',s)
#print re.findall(r'\A\d',s)
#print re.findall(r'\A.',s)

                    #\Z 从字符串末尾进行匹配
#print re.findall(r'\W\Z',s)

                    # ^ 从每行开头
'''
print re.findall(r'^\w',s)
print re.findall(r'^\d',s)
print re.findall(r'^.',s)
'''
                    # $ 从每行末尾
#print re.findall(r'\W$',s)

                    #[] 匹配中括号当中任意一种
#print re.findall(r'[aom]',s)
#print re.findall(r'[123]','15791579')
#print re.findall(r'[\s\d]',s)
#print re.findall(r'1[3578]','15378732778128913754785787887183234324324233')
'''
15 
18
13
17
'''
                    # | 匹配管道符两边任意一边
#print re.findall(r'13|15|18','178732778128917547857878871832')

                    #[^...] 非
'''
print re.findall(r'[^\d]',s)
print re.findall(r'\D',s)
'''
#print re.findall(r'[^\w]',s)

                    #[a-z] 匹配一个范围
#print re.findall(r'[a-z]',s)
#print re.findall(r'[A-Z]',s)
#print re.findall(r'[f-k]',s)
#print re.findall(r'[0-9]',s)
#print re.findall(r'[a-zA-Z]',s)
#print re.findall(r'[A-Z0-9]',s)

                    #() 组匹配，当组匹配出现的时候，其他的匹配方式作为组匹配的条件进行匹配
#print re.findall(r'\w\d',s)
#print re.findall(r'(\w)\d',s)
#print re.findall(r'\w\w',s)
#print re.findall(r'\w(\w)',s)

                    #(?P<name>...) 命名组
#print re.findall(r'(?P<laoli>\s)',s)
a = 'b3b c2d e5e f7h g8g l2u'
#print re.findall(r'(?P<xiaoli>\w)',a)
                    #(?P=name)  调用命名组匹配到的结果
#print re.findall(r'(?P<xiaoli>\w)\d',a)
#print re.findall(r'(\w)\d',a)
#print re.findall(r'(?P<xiaoli>\w)\d(?P=xiaoli)',a)
'''
b 3 b
c 2 c
e 5 e
f 7 f
g 8 g
l 2 l
'''
                    #(.*) 贪婪匹配
#print re.findall(r'a(.*)b','acc12345ccc\naaaacccb')
#print re.findall(r'a(.*)b','abbbbbbbbb')

                    #(.*?) 反贪婪匹配
#print re.findall(r'a(.*?)b','abbbbbbbbb')

a = 'b3b c2d e5e f7h g8g l2u'
                    #(?=...) 前瞻断言匹配
#print re.findall(r'\w(?=\d)',a)
#print re.findall(r'\w(?=\d)\w',a)
                    #(?!...) 反前瞻断言匹配
#print re.findall(r'\w(?!\d)',a)

                    #(?<=...) 后顾断言匹配
#print re.findall(r'(?<=\d)\w',a)
                    #(?<!...) 反后顾断言匹配
#print re.findall(r'(?<!\d)\w',a)
#print re.findall(r'\D',a)

                #匹配数量的规则
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."  
                    #* 匹配0到多次
#print re.findall(r'\w*',s)

                    #+ 匹配1到多次
#print re.findall(r'\w+',s)

                    #? 匹配0到1次
#print re.findall(r'\w?',s)

                    #{3} 匹配指定次数
#print re.findall(r'\w{3}',s)

                    #{1,4} 匹配1到4次
#print re.findall(r'\w{1,4}',s)

                #特殊规则
                    #re.I 忽略大小写
s = 'aAbBcCdDeAfAg'
#print re.findall(r'a',s,re.I)

                    #re.S 修改.的匹配方式
s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."
#print re.findall(r'.',s,re.S)

                    #re.M 多行模式
s = '''My name is xiao_wang,\n
I'm 24 years old,\t
my job is ITmonkey.'''

#print re.findall(r'\A\w',s,re.M)
#print re.findall(r'^\w',s,re.M)
#print re.findall(r'.\Z',s,re.M)
#print re.findall(r'.$',s,re.M)


            #匹配的方法
                #findall 在指定字符串当中查找所有满足正则表达式描述的内容，返回列表形式
#print re.findall('m',s)

s = "My name is xiao_wang,\n I'm 24 years old,\t my job is ITmonkey."
                #search 在指定的字符串当中查找符合正则表达式描述的内容，如果存在，返回匹配对象（第一次匹配到的结果）
                        #如果不存在，返回None
m = re.search(r'\w+',s)
#print re.search(r'aaa',s)
#print dir(m)
#print m.group()
#print re.search(r'\d',s).group()

#匹配对象
    #group
    #groups
                #match 在指定字符串的开头查找符合正则表达式描述的内容，如果存在，返回匹配对象（第一次匹配到的结果）
                        #如果不存在，返回None
#print re.match(r'\w+',s).group()
#print re.match(r'\d+',s)
#print re.match(r'aaa',s)
#print re.match(r'\s',s)

#print re.match(r'(\w+)(.)(\w+)(.)',s).groups()
#print re.match(r'(\w+)',s).groups()
#print re.search(r'(\d)(\d)',s).groups()

                #sub将匹配到的内容替换为指定的字符
'''
print re.sub(r'\w','*',s)
print s
#print re.findall(r'\w+',s)
'''
#print re.sub(r'\w+','$',s,5)

                #split 按照匹配的内容切分字符串
'''
print len(re.split(r'\s',s))
print len(re.findall(r'\s',s))
'''
#print re.split(r'\s',s,4)
                #compile 形成一个正则模板
c = re.compile(r'\w')
#print c.findall(s)
#print c.findall(s,10,20)
#print re.findall(r'\w',s)
#print re.findall(c,s)


#结构匹配
    #lxml  BeautifulSoup



#匹配11位手机号
#匹配邮箱
#匹配IP
s = '12.12.12.12'
#print re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',s).group()

#匹配身份证号18 X  15
#re.findall(r'\d{18}|\d{17}X|\d{15}')



html = '''
<html>
    <head>
        <title>
            hello
        </title>
    </head>
    <body>
        <p>
            "你个废连用毒这种卑鄙的伎俩也能用的出来简直丢光了你们萧家的人"<br/>"白纸黑字这座金矿这次归我们凌家了"<br/>"你个废物连给我提鞋都不配滚吧"
        </p>
    </body>
</html>
'''
#print re.findall(r'<p>(.*?)</p>',html,re.S)


for i in re.findall(r'<p>(.*)</p>',html,re.S):
    pass
    #print i
    #print i.replace('<br/>','\n')

