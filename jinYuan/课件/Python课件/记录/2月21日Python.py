Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print2267+0x2bf4

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print2267+0x2bf4
NameError: name 'print2267' is not defined
>>> 2267+0x2222
11005
>>> print(2267+0x2345)
11296
>>> print"this is jingyuanwanbo"
this is jingyuanwanbo
>>> 87<23
False
>>> 0xff==255
True
>>> 0xff==222
False
>>> print n=123
SyntaxError: invalid syntax
>>> print'n=123'
n=123
>>> n=123
>>> print n
123
>>> n=123
>>> f=2445.234
>>> s1='Hello,world'
>>> s2'hello\'harry''
SyntaxError: invalid syntax
>>> s2='hello\'harry''
SyntaxError: EOL while scanning string literal
>>> s2='hello\'harry\''
>>> print f  n  s1  s2
SyntaxError: invalid syntax
>>> print f,n,s1,s2
2445.234 123 Hello,world hello'harry'
>>> 
