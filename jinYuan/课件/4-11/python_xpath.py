#coding:utf-8

from lxml import etree

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
        <h1 class="heading">Hello world Top News</h1>
        <h1 style = "color:red;">Hello world</h1>
        <p style="font-size: 200%">World News only on this page</p>
        <div>
            <p style = "font-weight:700;">... and this is a parsed fragment ...</p>
            <p>Ah, and here's some more text, by the way.</p>
        </div>
        <a href="http://www.cydf.org.cn/" rel="nofollow" target="_blank">青少年发展基金会</a>
        <a href="http://www.4399.com/flash/32979.htm">洛克王国</a>
        <a href="http://www.4399.com/flash/35538.htm" target="_blank">奥拉星</a>
        <a href="http://game.3533.com/game/">手机游戏</a>
        <a href="http://game.3533.com/tupian/" target="_blank">手机壁纸</a>
        <a href="http://www.4399.com/" target="_blank">4399小游戏</a>
        <a href="http://www.91wan.com/" target="_blank">91wan游戏</a>
    </body>
</html>
'''

page = etree.HTML(html.decode('utf-8'))
#print dir(page)
#a = page.xpath('/html/body/a')
a = page.xpath('//a')
#p = page.xpath('/html/body/p')
p = page.xpath('//p')
for i in p:
    #print dir(i)
    #print i.text
    #print i.attrib
    #print i.tag
    #print i.values()
    #print i.keys()
    pass

p = page.xpath('//p[position() = 1]')
#print p[0].text

a = page.xpath('//a[4]')
#print a[0].text

'''
a = page.xpath('//a[position() > 3]')
for i in a:
    print i.text
'''
p = page.xpath('//p[@style="font-size: 200%"]')
#print p[0].text

#a = page.xpath('//a[@rel="nofollow"]')
a = page.xpath('//a[@target="_blank"]')
#print a[0].text
for i in a:
    #print i.text
    pass

h = page.xpath('//h1[text() = "Hello world"]')
#print h[0].attrib

h = page.xpath('/html/body/h1[contains(text(),"Hello world")]') #选取节点文本包含Hello world的h1节点 
#print h[0].attrib
#print h

a = page.xpath('//a[3][@target="_blank"]')
#print a[0].text

a = page.xpath('//a[@target="_blank"][3]')
#print a[0].text

p = page.xpath('/html/body/*/p')
'''
for i in p:
    print i.text
'''

p = page.xpath('/descendant::p')
#print p

t = page.xpath(u"/descendant::*[text()]") #表示任意多层的中间节点下任意标签之间的内
#print t

'''
a = page.xpath('//a[not(@target="_blank")]')
for i in a:
    print i.text
'''
#print page.xpath('//p/parent::*')    父节点
#print page.xpath('//h1/ancestor::*') 祖先节点
#print page.xpath('//body/child::*')  子节点
#print page.xpath('//body/descendant::*')  后代节点
