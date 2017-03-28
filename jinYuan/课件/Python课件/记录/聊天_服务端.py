#coding:gbk
import socket

'''
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
soc.bind(('127.0.0.1',9000))
soc.listen(3)
con,add = soc.accept()
#print con
#print add
f = open('123.txt','r')
content = f.read()
#con.send('I am your server')
con.send(bytes(content))
print con.recv(512)
f.close()
soc.close()
'''
class Myserver():
    def __init__(self):
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.soc.bind(('127.0.0.1',8008))
        self.soc.listen(3)
        self.con,self.add = self.soc.accept()
        while True:
            self.recvs = self.con.recv(512)
            if self.recvs == 'ByeBye':
                print self.recvs
                break
            else:
                print self.recvs

            self.sends = raw_input('Please enter you want to say:')
            if self.sends == '886':
                self.con.send(self.sends)
                break
            else:
                self.con.send(self.sends)
        
        self.soc.close()

if __name__ == '__main__':
    server = Myserver()

