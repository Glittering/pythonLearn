#coding:gbk

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('127.0.0.1',9009))

while True:
    sends = raw_input('Please enter you want to say:')

    if sends == 'Bye':
        sock.send(sends)
        break
    else:
        sock.send(sends)

    recvs = sock.recv(512)
    if recvs == '886':
        print recvs
        break
    else:
        print recvs


sock.close()
