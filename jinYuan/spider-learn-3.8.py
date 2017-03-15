#coding:UTF-8

import urllib,urllib.request,  re

#print help(urllib.urlopen)
#print 
#print dir(urllib2)

#response = urllib2.urlopen("http://www.baidu.com")
#print dir(response)
#print response.read()

#request = urllib2.Request('http://www.baidu.com')
#response = urllib2.urlopen(request)
#print response.read()
#help(urllib2.Request())

values={
	'username' : '11111',
	'password' : '2222'
}
#print type(values)
#print type(urllib.urlencode(values))

url = 'http://www.qiushibaike.com/'
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {'User-Agent':user_agent}
request = urllib.request(url,None,headers)
response = urllib.urlopen(request)
#response = urllib.request.urlopen(url,None,headers)
content = response.read()
#print content

#result = re.findall(r'<div class="content">(.*?)</div>',content,re.S)
#for i in result:
#    print i

from lxml import etree

tree = etree.HTML(content.decode('UTF-8'))

a = tree.xpath("//div[@class='content']/span")
print (a.text)


