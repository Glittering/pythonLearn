#spider
1.调度程序
2. URL管理器
    插入，去重
    读取，查询是否已读，变已读
3. 网页下载器
+ urllib2
    1. urllib2.open(url)
        response = ...
	response.getcode()==200 表示成功
    2. url data header
        urllib2.Request(url,data,header)
	urllib2.open(request)
    3. 特殊情景处理器
        HTTPCookieProcessor
	ProxyHandler
	HTTPSHandler
	HTTPRedirectHandler

	op=urllib2.build_opener(handler)
	urllib2.open(op)
+ requests
4. 网页解析器
+ 正则
+ html.parser
+ BeautifulScoup 
**安装**:pip install beautifulsoup4
1.创建BS对象
2.搜索节点 **find_all** **find**
3.访问节点:名称。属性。文字。
- *内容，解析器，编码*
- *find_all(内容，解析器，编码)*
  *find()*
- **访问节点信息** *:.name;['href'];.get_text()*
+ lxml

--------------
1. Python3不像2x中酷虎的和服务器模块结构散乱，Python3中把这些打包成为了2个包，就是http与urllib，详解如下：
http会处理所有客户端--服务器http请求的具体细节，其中：    
（1）client会处理客户端的部分
（2）server会协助你编写Python web服务器程序
（3）cookies和cookiejar会处理cookie，cookie可以在请求中存储数据

2. urllib是基于http的高层库，它有以下三个主要功能：
（1）request处理客户端的请求
（2）response处理服务端的响应
（3）parse会解析url
---------------
**urlparse**.urljoin(a1,a2)
	将a2 按照 a1 的格式拼接
---------------
soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
links = soup.find_all('a', herf=re.compile(r'/view/\d+\.htm'))
for link in links:
    link = link['href']

