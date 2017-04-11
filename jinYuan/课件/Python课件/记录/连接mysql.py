#coding:gbk

#mysql -u用户名 -p密码 

    #增
        #create database dbname;
        #create table tname(id int,name varchar(30));
        #insert into tname(name) values();
        #alter table tname add stu_num int not null;
        
    #删
        #drop database dbname;
        #drop table table;
        #delete table tname where id=1;
        #alter table tname drop cname;
        #truncate tname; 

    #改
        #update tname set cname=value where id=2;
        #alter table tname change old_cname new_cname int not null;

    #查
        #desc tname;
        #select * from tname;
        #select * from tname limit 3;
        #select * from tname order_by cname;
        
    #给权限
        #grant all on dbname.* to uname@localhost identified by'password';

#python 安装模块
    #.exe
    #压缩包 解压，在CMD中切换目录，切到解压目录之下找到setup.py，执行python setup.py install
    #pip install MySQL-python==1.2.5

import MySQLdb

#1、创建连接对象
    #connect
        #host 主机名
        #user 用户名
        #passwd 密码
        #db   库名
        #port 3306
        #charset 

con = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '121',
    db = 'aaa'
    )
#print con

#2、实例化游标
    #游标（游标缓冲区）：是存储数据库返回给python数据的一片空间
cur = con.cursor()

#3、执行sql语句
    #execute 执行单条sql语句

#cur.execute('create table student(id int,name varchar(30))')
#cur.execute("insert into student values(1,'xiaoqiang')")
#cur.execute('insert into student values(2,%s)','xiali')
#cur.execute('insert into student(id) values(%d)'%3)

    #executemany 执行单条sql语句，重复执行执行参数列表里面的参数

#cur.executemany('insert into student(id) values(%s)',range(4,10))
#cur.executemany('insert into student(name) values(%s)','abcdefg')

#cur.execute('select * from student')
'''
for i in cur.fetchall(): #查看所有数据
    print i
'''
#print cur.fetchone()  #查看一条数据
#print cur.fetchmany(4) #查看多条数据


#4、关闭连接
#con.commit()   #提交
#com.rollback() #回滚


cur.close()
con.close()



#python sqlite3
import sqlite3

conn = sqlite3.connect('F:\lianxi\hello.db')
cur = conn.cursor()
cur.execute("insert into teacher values('laoli')")
cur.execute('select * from teacher')
print cur.fetchall()

conn.commit()
cur.close()
conn.close()
