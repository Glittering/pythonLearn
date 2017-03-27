#coding:gbk

import socket,SocketServer

#数据传输
    #协议
        #TCP:面向连接的协议，造价比较高，准确性高
        #UDP:无连接的协议，造价比较低，准确性差

#被动的阻塞式的连接
    #单工：只有一条信道，通信双方不可逆
    #半双工：只有一条信道，通信双方可逆
    #全双工：有多条信道，通信双方可逆


#服务端套接字编程
    #1、创建socket对象
        #socket.socket()
            #family
                #AF_INET 网络间的、跨平台的
                #AF_UNIX 系统内部的
                #AF_INET6
            #type
                #SOCK_STREAM --> TCP
                #SOCK_DGRAM  --> UDP

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2、绑定IP和端口号
        #bind 需要一个双元素元组
            #port 65535  1024以下公共服务端口号
soc.bind(('127.0.0.1',8000))

    #3、监听端口个数
        #listen
soc.listen(3)

    #4、数据处理阶段
        #accept
            #接收一个新的socket对象
            #客户端身份
con,add = soc.accept()

        #接收和发送数据
            #recv
            #send
con.recv(512)
con.send('I am your server')

    #5、关闭socket对象
        #close
soc.close()



#客户端套接字编程
    #1、创建socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2、连接服务端
        #connect 需要一个双元素元组
sock.connect(('127.0.0.1',8000))

    #3、接收和发送数据
sock.send('I am your client')
sock.recv(512)

    #4、关闭socket对象
        #close
sock.close()



