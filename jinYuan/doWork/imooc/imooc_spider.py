#!/usr/lib/python3.5
import re
from bs4 import BeautifulSoup;
import urllib,urllib2;

html='http://www.baidu.com'
user_agent = 'Mozilla/5.0'
heards={'User-Agent':user_agent}
valus={'username':'1111','password':'2222'}
valus=urllib.urlencode(valus)
reqest = urllib2.Request(html,valus,heards)
content = urllib2.urlopen(reqest)

#print content
soup = BeautifulSoup(content.read(),'html.parser',from_encoding='utf-8')

print 'get all links'
links = soup.find_all('a')
for i in links:
    print i.name, i['href'], i.get_text()

print 'get juBao\'s link'
i = soup.find('a',href='http://www.baidu.com/search/jubao.html')
print i.name, i['href'], i.get_text()

print 'use re'
i = soup.find('a',href=re.compile(r'ques'))
print i.name, i['href'], i.get_text()

print 'get label p'
links = soup.find_all('p')
for i in links:
    print i.name, i.class_, i.get_text()


