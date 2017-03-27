#coding:gbk

import socket

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('',9009))
soc.listen(5)

con,add = soc.accept()
#print con
#print add
while True:
    recvs = con.recv(512)
    if recvs == 'Bye':
        print recvs
        break
    else:
        print recvs
        
    sends = raw_input('Please enter you want to say:')

    if sends == '886':
        con.send(sends)
        break
    else:
        con.send(sends)
    
soc.close()
