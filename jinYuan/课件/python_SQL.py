#coding:gbk

#mysql -uroot -p 密码

#增
    #create database dbname;
    #create table tname(id int,name varchar(30));
    #insert into tname(cname,...) values();
    #alter table tname add gender char(10) not null;

#删
    #drop database dbname;
    #drop table tname;
    #delete from tanme where id=1;
    #truncate tname;
    #alter table tname drop cname;

#改
    #alter table tname change name name varchar(30) not null;
    #update tname set name='xxxx' where id=1;
    

#查
    #desc tname;
    #select cname,cname from tname;
    #select * from tname;

#给权限
    #grant all on *.* to uname@localhost identified by'密码';


import MySQLdb

#1、创建连接对象
    #connect
        #host
        #user
        #passwd
        #db
        #charset
        #port
con = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '121',
    db = 'aaa'
)

#print con
#2、实例化游标
    #游标：是系统为用户开设的一个数据缓冲区，存放SQL语句的执行结果
cur = con.cursor()

#3、执行sql语句
    #execute 执行单条sql语句
    #executemany 执行单条sql语句，重复执行参数列表里面的参数

#cur.execute('create table teacher(id int,name varchar(50));')
#cur.execute("insert into teacher values(1,'laochen')")
'''
for i in ['xiaozhen','laoli','laojiang']:
    cur.execute("insert into teacher(name) values(%s)",i)
'''
#cur.executemany('insert into teacher(id) values(%s)',range(5))

#cur.execute('insert into teacher(id) values(%s)'%100)
#cur.execute('alter table teacher add age int')

cur.execute('select * from teacher')

#print cur.fetchone() #查看一条数据
#print cur.fetchmany(3) #查看多条数据
#print cur.fetchall() #查看所有数据


#4、关闭连接

con.commit()
#con.rollback()

cur.close()
con.close()



#python 异常处理
    #程序结构上或者逻辑上的错误

    #几种常见的异常种类
        #TypeError
        #SyntaxError
        #NameError
        #AttributeError
        #KeyError
        #StopIteration

'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    except:
        print 'hello world'

'''
#Exception 所有异常的基类
'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    except Exception,e:
        print e
'''
'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    except NameError,e:
        print e

    except TypeError,e:
        print e
'''
'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    
    except:
        print '哈哈，你错了'

    finally:
        print '一切都结束啦'

'''
'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    
    except:
        print '哈哈，你错了'

    else:
        print '一切都结束啦'
'''

'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    
    except:
        print '哈哈，你错了'

    else:
        print '哦，恭喜'

    finally:
         print '一切都结束啦'
'''

#raise 诱发异常
'''
raise TypeError('abcdefg')
for i in range(10):
    print i
    raise NameError('错啦')
'''


import sqlite3

#1、创建连接对象
#con = sqlite3.connect('hello.db')
con = sqlite3.connect('F:\myblog\db.sqlite3')
#print con

#2、实例化游标
cur = con.cursor()
#3、执行sql语句
cur.execute('select * from auth_user')
#cur.execute('select * from teacher')
print cur.fetchall()

#4、关闭连接

cur.close()
con.close()
