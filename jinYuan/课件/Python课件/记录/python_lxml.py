#coding:utf-8
from lxml import etree
import re

html = '''
<html>
    <head>
        <meta name="content-type" content="text/html; charset=utf-8" />
        <title>友情链接查询 - 站长工具</title>
        <!-- uRj0Ak8VLEPhjWhg3m9z4EjXJwc -->
        <meta name="Keywords" content="友情链接查询" />
        <meta name="Description" content="友情链接查询" />
    </head>
    <body>
        <h1 class="heading">Top News</h1>
        <p style="font-size: 200%">World News only on this page</p>
        Ah, and here's some more text, by the way.
        <p>... and this is a parsed fragment ...</p>
        <a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>
        <a href="http://www.4399.com/flash/32979.htm" target="_blank">洛克王国</a>
        <a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>
        <a href="http://game.3533.com/game/" target="_blank">手机游戏</a>
        <a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
        <a href="http://www.4399.com/" target="_blank">4399小游戏</a>
        <a href="http://www.91wan.com/" target="_blank">91wan游戏</a>
        <div>
            <p>
                Ah, and here's some more text, by the way.
            </p>
            <h1>Top News</h1>
        </div>
        <p>
            hello
        </p>
    </body>
</html>
'''

'''
html = html.decode('utf-8')
con = re.findall(r'<a.*>(.*)</a>',html)

for i in con:
    print i
'''


content = etree.HTML(html.lower().decode('utf-8'))
#print content
href = content.xpath('/html/body/a') #-- '//a'
for i in href:
    #print i.attrib
    #print i.text
    pass
#print dir(i)

'''
p = content.xpath('//p')
for i in p:
    print i.text
'''
p = content.xpath('//p[@style="font-size: 200%"]')
#print p[0].text
#print p[0].values()

href = content.xpath('//a[@href="http://www.4399.com/flash/35538.htm"]')
#print href[0].text

p = content.xpath("//p[position()=1]")
print p[0].text
