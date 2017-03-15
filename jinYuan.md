pip的网站，搜pypi

匹配的模块，re  lxml  BeautifulSoup

#cgi模块

查apache  httpd

web框架	flask  django   特纳豆？

service /etc/init.d/apache2 start

问  正则

#lxml

content = etree.HTML(html.lower())
href = conetnt.xpath('//a')

xpth中可以用 绝对路径
	或者 相对路径 //代表左右层级


a,b = b,a + b  什么东西

#urllib
1. urllib

2. urllib2
urlopen 可以打开 r = urllib2.Request(url) 
	r.add_header('User-Agent','awesome fetcher')
	r.add_data(urllib.urlencode({'foo':'bar'}))
	response = urllib2.urlopen(r)

#据说是复习
1. 模块
   + time datetime calendar
       - time.time()
       - time.localtime()
       - time.gmtime()
       - time.asctime()
       - time.ctime()
       - time.mktime()
       - time.sleep()
       - time.clock()
       - time.strftime()
   + wx
       - app = wx.App()
         frame = wx.Frame(None)
	 panel = wx.Panel(frame)
	 frame.Show()
	 app.MainLoop()
       - Frame
           * parent
	   * id
	   * title
	   * size
	   * pos
	   * style
	   * name
       - Button
           * lable
       - TextCtrl
           * value
       - 尺寸器布局
           *panel
	   *创建尺寸器
               BoxSizer
	           wx.VERTICAL
           *添加组件
	       Add
	           name
		   pro
       -
       -
   + ConfigParser    配置文件
       - ConfigParser.ConfigPaerser()
           * read()
	   * sections()
	   * options()
	   * items()
	   * get()
	   * remove_section()
	   * remove_option()
	   * add_section()
	   * set()
	   * has_option
	   * has_section()
	   * write(open(path,mode))
   + lxml
       - etree
           * xpath
	       //
	       /
	       @
	       position()
	       test()
	       contains(text(),'')
   + random
       - random.random()
       - random.choice()
       - random.shuffle()
       - random.randint()
       - random.uniform()
       - random.sample()
       - random.randrange()
   + socket
       - socket.socket()
           * family
	       AF_INET
	       AF_UNIX
	   * type
	       SOCK_STREAM  --> tcp
	       SOCK_DGRAM   --> udp
       - bind()
       - listen()
       - accept()
           * 新的套接字对象
	       send sendall
	       recv()
	   * 客户端的身份
       - close()

       ***客户端***
   + threed
   + threeding
   + Queue
   + urllib urllib2
   + os
   + sys
   + re
   + cgi
   + math
   + MySQLdb
   + sqlite3
   + logging
   + keyword


#2017年 03月 13日 星期一 14:04:52 CST

1. pygame

2. \v 垂直制表符

3. str 的方法
    + 格式化	format
    + 切分	split 从左到右切分， rsplit 从右到左
        ('字符串',num)  以字符串切分，num次
    + 删减
        strip('') 空的会删除空白。有字符就会删除
    + 拼接
        join 将可迭代对象拆分，循环添加进去
	*\+*
    + 替换
        replace
    + 查找
        find   找不到返回-1
        index  找不到报错
        count  统计出现次数
    + 变形
        upper()
	lower()
	title()		首字母大写
	capitalize()	首字母大写，其他小写
	swapcase()	大小写互换
    + 填充
        center()	s.center(30,'a')  用a填充并居中,
	ljust() rjust() 左右对齐
	zfill()		用0填充
	expandtabs()	用指标符分隔
    + 判断
        isupper()	判断是否完全大写
	islower()	
	istitle()
	isdigit()	数字
	isalpha()	字母
	isalnum()	是否完全由数字或字母组成
	startswitch()	以..开始
	endswitch()	已..结束，后两位索引
    + 编码
        encode		加码
	decode		解码

#2017年 03月 14日 星期二 14:47:15 CST
1. list
    + 添加
        append
	extend	将可迭代对象拆分，依次添加到列表中
	insert	
    + 查找
        index
	count
    + 删除
        pop
	del
	remove
    + 排序
        sort
        reverse		按照索引倒排序
2. tuple
    index	count

3. dict
    keys
    values
    items
    get('key',default) 	key is not exist , print default
    setdefault()	key is not exist , add the default(None)
    update()		adb = 1000  the key is a varite not string
    has_key
    in
    clear		clear the dict , but the object exist still
    pop
    popitem		random pop a key:values
4. set
5. array
    import numpy	from numpy import array


#the different betten 2 and 3
1. 2中有*Long*，3没有
2. 整形数相除，2中不会边浮点，3会边。
3. 3中有*字节*类型
4. 2中有repr()
5. print 2中是个字符串，3中是方法
6. *has_key* is covered by *in*


**doTheThings**:
1. *args* and **args**
2. find 和index 的区别
3. 加码，解码
4. utf-8和unicode
5. range() 2中是生成一个lista 3中返回一个range对象
6. xrange() 3中取消了。 返回一个xrange对象
7. 


**字符串逆序**
1. 字符串的方法
2. ''.join(list[::-])
3. ''.join(l.reverse())

**一些方法**
1. org() 查看 ascii
2. sorted()  reversed()
3. zip() 将序列相同索引上的元素合并到元组当中，返回列表形式
4. map() 同zip，以长序列为主
5. in
