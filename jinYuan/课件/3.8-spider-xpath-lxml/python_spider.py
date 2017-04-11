#coding:gbk

#python 爬虫：在万维网上，模拟浏览器向服务器发送请求，服务器返回给我们数据
    #数据获取
        #urllib2 urllib request Cookie cookielib htmllib xmllib

    #数据过滤
        #字符串简单的处理方式
        #re
        #lxml
        #BeautifulSoup

    #数据存储
        #文件
        #数据库

import urllib,urllib2,re

#print dir(urllib)
#print dir(urllib2)


response = urllib2.urlopen("http://www.baidu.com")
#print dir(response)
#print response.read()


request = urllib2.Request('http://www.baidu.com')
response = urllib2.urlopen(request)
#print response.read()

#模拟登陆

values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "1234abcd"
user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
referer = "https://hao.360.cn/?src=lm&ls=n406c240298"

headers = {'User-Agent':user_agent,'Referer':referer}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"

request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
#print response.read()


user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
headers = {'User-Agent':user_agent}
url = "http://www.qiushibaike.com/"

request = urllib2.Request(url,None,headers)
response = urllib2.urlopen(request)
content = response.read()
#print content

result = re.findall(r'<div class="content">(.*?)</div>',content,re.S)
'''
thefile = open('1.doc','w')
for i in result:
    thefile.write(i.replace('<br/>','\n'))

thefile.close()
''' 
from lxml import etree   

'''
tree = etree.HTML(content.decode('utf-8'))

a = tree.xpath("//div[@class='content']/span")
#print a

for i in a:
    print i.text
'''


