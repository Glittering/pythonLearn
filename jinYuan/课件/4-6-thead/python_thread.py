#coding:gbk

#python 多线程

#进程：程序的一次运行，又称为重量级的进程
#线程：进程下的分支，又称轻量级的进程

#异步并发
    #时间片

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
#GIL:保证同一物理时间下只有一个线程在运行

'''
loops = [2,4]  #不但确定了线程的个数，还确定了线程的运行时间和锁的个数

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
        t = threading.Thread(target = loop,args = (i,loops[i])) #生成线程
        threads.append(t)

    for i in nloops:
        threads[i].start() #开始执行线程

    for i in nloops:
        threads[i].join()  #程序挂起，直到线程结束
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
        t = threading.Thread(target = loop,args = (i,loops[i])) #生成线程
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



