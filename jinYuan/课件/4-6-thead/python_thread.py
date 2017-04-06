#coding:gbk

#python ���߳�

#���̣������һ�����У��ֳ�Ϊ�������Ľ���
#�̣߳������µķ�֧���ֳ��������Ľ���

#�첽����
    #ʱ��Ƭ

import thread,threading
from time import ctime,sleep

'''
def loop0():
    print 'start loop0 at:',ctime()
    sleep(2)
    print 'loop0 done at:',ctime()

def loop1():
    print 'start loop1 at:',ctime()
    sleep(4)
    print 'loop1 done at:',ctime()

def main():
    print 'starting all at:',ctime()
    loop0()
    loop1()
    print 'all done at:',ctime()

main()
'''
'''
def loop0():
    print 'start loop0 at:',ctime()
    sleep(2)
    print 'loop0 done at:',ctime()

def loop1():
    print 'start loop1 at:',ctime()
    sleep(4)
    print 'loop1 done at:',ctime()

def main():
    print 'starting all at:',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    sleep(4)
    print 'all done at:',ctime()

main()
'''
#GIL:��֤ͬһ����ʱ����ֻ��һ���߳�������

'''
loops = [2,4]  #����ȷ�����̵߳ĸ�������ȷ�����̵߳�����ʱ������ĸ���

def loop(nloop,nsec,lock):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()
    lock.release()

def main():
    print 'starting all at:',ctime()
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        thread.start_new_thread(loop,(i,loops[i],locks[i]))
    sleep(5)
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()
'''
'''
loops = [2,4]
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting all at:',ctime()
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i])) #�����߳�
        threads.append(t)

    for i in nloops:
        threads[i].start() #��ʼִ���߳�

    for i in nloops:
        threads[i].join()  #�������ֱ���߳̽���
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()
'''
'''

loops = [2,4]
def loop(nloop,nsec):
    print 'start loop',nloop,'at:',ctime()
    sleep(nsec)
    print 'loop',nloop,'done at:',ctime()

def main():
    print 'starting all at:',ctime()
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        t = threading.Thread(target = loop,args = (i,loops[i])) #�����߳�
        threads.append(t)

    for i in nloops:
        threads[i].start()
        #print threads[i].isAlive()
        #print threads[i].getName()
        threads[i].setName('xiaoqiang')
        print threads[i].getName()

    for i in nloops:
        threads[i].join()
        #print threads[i].isAlive()
    print 'all done at:',ctime()

if __name__ == '__main__':
    main()
'''
'''
class Mythread(threading.Thread):
    def __init__(self,nloop,nsec):
        self.nloop = nloop
        self.nsec = nsec
        threading.Thread.__init__(self)

    def run(self):
        print 'start loop',self.nloop,'at:',ctime()
        sleep(self.nsec)
        print 'loop',self.nloop,'done at:',ctime()

if __name__ == '__main__':
    print 'starting all at:',ctime()
    loops = [2,4,5]
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = Mythread(i,loops[i])
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print 'all done at:',ctime()       
'''



