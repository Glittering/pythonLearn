#coding:gbk

#python ������

#����˺Ϳͻ���

#����������ʽ������
    #������ֻ��һ���ŵ���ͨ��˫��������
    #��˫����ֻ��һ���ŵ���ͨ��˫������  <-- socket���
    #ȫ˫�����ж����ŵ���ͨ��˫������

#URL:ͳһλ�ö�λ�� 
    #Э�� ���ݴ���
    #������IP
    #��Դ·��

#URI:ͳһλ�ñ�ʶ��

#Э��
    #TCP �������ӵ�Э�飬�Ƚϰ���׼ȷ�Ը�
    #UDP �����ӵ�Э�飬�Ƚ����ۣ�׼ȷ�Ե�

import socket

#������׽��ֱ��
    #1������socket����
        #family
            #AF_INET  �����ġ���ƽ̨��  -->IPV4
            #AF_UNIX  ϵͳ�ڲ���
            #AF_INET6 --> IPV6
        #type
            #SOCK_STREAM --> TCP
            #SOCK_DGRAM  --> UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#print sock
#print dir(sock)
    #2����IP��port
        #bind ��Ҫһ��˫Ԫ��Ԫ��
        #65535 1024����
sock.bind(('127.0.0.1',9000))

    #3������
        #listen
sock.listen(5)

    #4�����ݴ���׶�
        #TCP
            #send   sendall
            #recv

        #UDP
            #sendto
            #recvfrom

soc,add = sock.accept()
soc.recv(512)
soc.send('I am your server')

    #5���ر�socket����
        #close
sock.close()



#�ͻ����׽��ֱ��
    #1������socket����
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #2�����ӷ����
        #connect ��Ҫһ��˫Ԫ��Ԫ��
sock.connect(('127.0.0.1',9000))

    #3�����պͷ�������

sock.send('I am your client')
sock.recv(512)

    #4���ر��׽��ֶ���
        #close

sock.close()



