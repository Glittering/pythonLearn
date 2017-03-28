#coding:gbk

#python 异常处理
    #异常：程序当中逻辑上或语法上的错误
    #几种常见的异常
        #NameError
        #TypeError
        #SyntaxError
        #AttributeError
        #ValueError
        #KeyError

    #捕获异常
'''
try:
    'hello' * 100
    print '你好'

except:
    print 'welcome to my world'
'''
    #Exception 所有异常的基类
'''
try:
    'hello' + 100
except Exception,a:
    print a
'''
'''
while True:
    try:
        a = 'hello' + input('Please Enter:')
        print a
    except TypeError:
        print '你好'
    except NameError,e:
        print e
    except SyntaxError:
        print '哈哈哈，你错啦！！！'
'''     
'''   
try:
    a = 'hello' + input('>>>')
    print a
except:
    print '你好'
finally:
    print 'hello world'
'''

'''
try:
    a = 'hello' + input('>>>')
    print a
except:
    print '你好'
else:
    print 'welcome to my world'
finally:
    print 'hello world'
'''

    #诱发异常
        #raise
'''
raise TypeError("啊哈哈哈哈")
while True:
    print 'hello world'
    #raise NameError("name 'hello is not defined'")
'''
