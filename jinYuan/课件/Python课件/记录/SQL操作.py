#coding:gbk

from sqlalchemy import *

#�����������
db = create_engine('mysql://root:121@localhost/aaa',echo = True)
#db = create_engine('sqlite3:///hello.db)

#����Ԫ��Ϣ
metadata = MetaData(db)

#����

users = Table('student',metadata,
            Column('id',Integer),
            Column('name',String(50)),
            Column('age',Integer)
)

#users.create()

#print list(users.columns)[1].name
#print dir(users)

#��������

i = users.insert()
#print i
#i.execute(id = 1,name = "laoli",age = 30)
i.execute({'id':2,'name':'xiaoqiang','age':20},
          {'id':3,'name':'xiaozhao','age':25}
          )

#�鿴����
s = users.select()
#print s
r = s.execute()
#print r.fetchone()
#print r.fetchall()
print r.fetchmany(3)
