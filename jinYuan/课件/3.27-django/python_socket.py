#coding:gbk

import socket,SocketServer

#���ݴ���
    #Э��
        #TCP:�������ӵ�Э�飬��۱Ƚϸߣ�׼ȷ�Ը�
        #UDP:�����ӵ�Э�飬��۱Ƚϵͣ�׼ȷ�Բ�

#����������ʽ������
    #������ֻ��һ���ŵ���ͨ��˫��������
    #��˫����ֻ��һ���ŵ���ͨ��˫������
    #ȫ˫�����ж����ŵ���ͨ��˫������


#������׽��ֱ��
    #1������socket����
        #socket.socket()
            #family
                #AF_INET �����ġ���ƽ̨��
                #AF_UNIX ϵͳ�ڲ���
                #AF_INET6
            #type
                #SOCK_STREAM --> TCP
                #SOCK_DGRAM  --> UDP

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2����IP�Ͷ˿ں�
        #bind ��Ҫһ��˫Ԫ��Ԫ��
            #port 65535  1024���¹�������˿ں�
soc.bind(('127.0.0.1',8000))

    #3�������˿ڸ���
        #listen
soc.listen(3)

    #4�����ݴ���׶�
        #accept
            #����һ���µ�socket����
            #�ͻ������
con,add = soc.accept()

        #���պͷ�������
            #recv
            #send
con.recv(512)
con.send('I am your server')

    #5���ر�socket����
        #close
soc.close()



#�ͻ����׽��ֱ��
    #1������socket����
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2�����ӷ����
        #connect ��Ҫһ��˫Ԫ��Ԫ��
sock.connect(('127.0.0.1',8000))

    #3�����պͷ�������
sock.send('I am your client')
sock.recv(512)

    #4���ر�socket����
        #close
sock.close()



