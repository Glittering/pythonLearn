# pythonDB

**python DB API**

### 流程
1. mk connection
2. mk cursor
3. do DB command
4. close cursor
5. close connection

### 环境
1. Eclipse + Pydev **Develop**
2. Python-MySQL connector  **python对数据库的访问能力**
3. 管理工具
4. mysql 服务器

## python 操作数据库对象

###connection  数据库链接对象
####MySQLdb.connect()
host 地址
port 端口号
user 用户名
passwd 密码
db 数据库名称
charset 链接编码
#### connection对象支持的方法
1. cursor() 创建并返回游标
2. commit() 提交当前事物
3. rollback() 回滚当前事物
4. close() 关闭链接

### cursor      游标对象
#### 方法
1. execute() 
2. fetchone() 取的结果集的下一行
3. fetchmany(size) 取的结果集的下几行
4. fetchall() 取的结果集中剩下的所有行
5. rowcount 最近一次execute返回数据的行数或影响行数
5. close() 关闭游标对象
*rownumber类似指针，遍历查缓冲区用的。*

## python 增删改查数据库

###select

###inset

###update

###delete

## 使用python实现实例

**新奇的玩意**
1. 格式化输出 print "userid=%s, username=%s"%row
