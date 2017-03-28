#coding:gbk
import socket
'''
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.connect(('127.0.0.1',9000))
recvs = soc.recv(512)
f = open('1.doc','w')
f.write(recvs)
soc.send(b'I am your client')
f.close()
soc.close()
'''
class Myclient():
    def __init__(self):
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.connect(('127.0.0.1',8008))
        while True:
            self.sends = raw_input('Please enter you want to say:')
            if self.sends == 'ByeBye':
                self.soc.send(self.sends)
                break
            else:
                self.soc.send(self.sends)

            self.recvs = self.soc.recv(512)
            if self.recvs == '886':
                print self.recvs
                break
            else:
                print self.recvs
        self.soc.close()

if __name__ == '__main__':
    client = Myclient()


