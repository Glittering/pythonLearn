#coding:gbk

#python �쳣����
    #�쳣���������߼��ϻ��﷨�ϵĴ���
    #���ֳ������쳣
        #NameError
        #TypeError
        #SyntaxError
        #AttributeError
        #ValueError
        #KeyError

    #�����쳣
'''
try:
    'hello' * 100
    print '���'

except:
    print 'welcome to my world'
'''
    #Exception �����쳣�Ļ���
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
        print '���'
    except NameError,e:
        print e
    except SyntaxError:
        print '�������������������'
'''     
'''   
try:
    a = 'hello' + input('>>>')
    print a
except:
    print '���'
finally:
    print 'hello world'
'''

'''
try:
    a = 'hello' + input('>>>')
    print a
except:
    print '���'
else:
    print 'welcome to my world'
finally:
    print 'hello world'
'''

    #�շ��쳣
        #raise
'''
raise TypeError("����������")
while True:
    print 'hello world'
    #raise NameError("name 'hello is not defined'")
'''
