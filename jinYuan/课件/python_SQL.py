#coding:gbk

#mysql -uroot -p ����

#��
    #create database dbname;
    #create table tname(id int,name varchar(30));
    #insert into tname(cname,...) values();
    #alter table tname add gender char(10) not null;

#ɾ
    #drop database dbname;
    #drop table tname;
    #delete from tanme where id=1;
    #truncate tname;
    #alter table tname drop cname;

#��
    #alter table tname change name name varchar(30) not null;
    #update tname set name='xxxx' where id=1;
    

#��
    #desc tname;
    #select cname,cname from tname;
    #select * from tname;

#��Ȩ��
    #grant all on *.* to uname@localhost identified by'����';


import MySQLdb

#1���������Ӷ���
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
#2��ʵ�����α�
    #�α꣺��ϵͳΪ�û������һ�����ݻ����������SQL����ִ�н��
cur = con.cursor()

#3��ִ��sql���
    #execute ִ�е���sql���
    #executemany ִ�е���sql��䣬�ظ�ִ�в����б�����Ĳ���

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

#print cur.fetchone() #�鿴һ������
#print cur.fetchmany(3) #�鿴��������
#print cur.fetchall() #�鿴��������


#4���ر�����

con.commit()
#con.rollback()

cur.close()
con.close()



#python �쳣����
    #����ṹ�ϻ����߼��ϵĴ���

    #���ֳ������쳣����
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
#Exception �����쳣�Ļ���
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
        print '�����������'

    finally:
        print 'һ�ж�������'

'''
'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    
    except:
        print '�����������'

    else:
        print 'һ�ж�������'
'''

'''
while True:    
    try:
        a = input('Please enter:')
        b = a + 'abc'
        print b
    
    except:
        print '�����������'

    else:
        print 'Ŷ����ϲ'

    finally:
         print 'һ�ж�������'
'''

#raise �շ��쳣
'''
raise TypeError('abcdefg')
for i in range(10):
    print i
    raise NameError('����')
'''


import sqlite3

#1���������Ӷ���
#con = sqlite3.connect('hello.db')
con = sqlite3.connect('F:\myblog\db.sqlite3')
#print con

#2��ʵ�����α�
cur = con.cursor()
#3��ִ��sql���
cur.execute('select * from auth_user')
#cur.execute('select * from teacher')
print cur.fetchall()

#4���ر�����

cur.close()
con.close()
