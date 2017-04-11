#coding:UTF-8
import cookielib
import urllib
import urllib2

print '----one----'
url = 'http://www.baidu.com'
content = urllib2.urlopen(url)
print content.getcode()
print len(content.read())

print '----two----'
request = urllib2.Request(url)
request.add_header('User-Agent','Mozilla/5.0')
data = {
    'username' : '11111',
    'password' : '22222'
}
data = urllib.urlencode(data)
request.add_data(data)
response = urllib2.urlopen(request)
# content = response.read()
print response.getcode()
print len(response.read())

print '----three----'
# cj = cookielib.CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# urllib2.install_opener(opener)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
content = urllib2.urlopen(url)
print content.getcode()
print cj
print len(content.read())
