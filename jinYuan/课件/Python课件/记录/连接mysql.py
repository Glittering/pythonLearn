#coding:gbk

#mysql -u�û��� -p���� 

    #��
        #create database dbname;
        #create table tname(id int,name varchar(30));
        #insert into tname(name) values();
        #alter table tname add stu_num int not null;
        
    #ɾ
        #drop database dbname;
        #drop table table;
        #delete table tname where id=1;
        #alter table tname drop cname;
        #truncate tname; 

    #��
        #update tname set cname=value where id=2;
        #alter table tname change old_cname new_cname int not null;

    #��
        #desc tname;
        #select * from tname;
        #select * from tname limit 3;
        #select * from tname order_by cname;
        
    #��Ȩ��
        #grant all on dbname.* to uname@localhost identified by'password';

#python ��װģ��
    #.exe
    #ѹ���� ��ѹ����CMD���л�Ŀ¼���е���ѹĿ¼֮���ҵ�setup.py��ִ��python setup.py install
    #pip install MySQL-python==1.2.5

import MySQLdb

#1���������Ӷ���
    #connect
        #host ������
        #user �û���
        #passwd ����
        #db   ����
        #port 3306
        #charset 

con = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = '121',
    db = 'aaa'
    )
#print con

#2��ʵ�����α�
    #�α꣨�α껺���������Ǵ洢���ݿⷵ�ظ�python���ݵ�һƬ�ռ�
cur = con.cursor()

#3��ִ��sql���
    #execute ִ�е���sql���

#cur.execute('create table student(id int,name varchar(30))')
#cur.execute("insert into student values(1,'xiaoqiang')")
#cur.execute('insert into student values(2,%s)','xiali')
#cur.execute('insert into student(id) values(%d)'%3)

    #executemany ִ�е���sql��䣬�ظ�ִ��ִ�в����б�����Ĳ���

#cur.executemany('insert into student(id) values(%s)',range(4,10))
#cur.executemany('insert into student(name) values(%s)','abcdefg')

#cur.execute('select * from student')
'''
for i in cur.fetchall(): #�鿴��������
    print i
'''
#print cur.fetchone()  #�鿴һ������
#print cur.fetchmany(4) #�鿴��������


#4���ر�����
#con.commit()   #�ύ
#com.rollback() #�ع�


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
