#coding:gbk

#python 网络编程

#服务端和客户端

#被动的阻塞式的连接
    #单工：只有一条信道，通信双方不可逆
    #半双工：只有一条信道，通信双方可逆  <-- socket编程
    #全双工：有多条信道，通信双方可逆

#URL:统一位置定位符 
    #协议 数据传输
    #域名或IP
    #资源路径

#URI:统一位置标识符

#协议
    #TCP 面向连接的协议，比较昂贵，准确性高
    #UDP 无连接的协议，比较廉价，准确性低

import socket

#服务端套接字编程
    #1、创建socket对象
        #family
            #AF_INET  网络间的、跨平台的  -->IPV4
            #AF_UNIX  系统内部的
            #AF_INET6 --> IPV6
        #type
            #SOCK_STREAM --> TCP
            #SOCK_DGRAM  --> UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print sock
#print dir(sock)
    #2、绑定IP和port
        #bind 需要一个双元素元组
        #65535 1024以下
sock.bind(('127.0.0.1',9000))

    #3、监听
        #listen
sock.listen(5)

    #4、数据处理阶段
        #TCP
            #send   sendall
            #recv

        #UDP
            #sendto
            #recvfrom

soc,add = sock.accept()
soc.recv(512)
soc.send('I am your server')

    #5、关闭socket对象
        #close
sock.close()



#客户端套接字编程
    #1、创建socket对象
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2、连接服务端
        #connect 需要一个双元素元组
sock.connect(('127.0.0.1',9000))

    #3、接收和发送数据

sock.send('I am your client')
sock.recv(512)

    #4、关闭套接字对象
        #close

sock.close()



