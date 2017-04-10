#coding:gbk

import Queue

#队列模式
    #Queue.Queue(maxsize) 先进先出
    #Queue.LifoQueue(maxsize) 先进后出
    #Queue.PriorityQueue(maxsize) 优先级别低的先出

'''
#q = Queue.Queue()
q = Queue.LifoQueue()
#print dir(q)
q.put('hello world')
for i in range(5):
    q.put(i)

#print q.get()
#print q.qsize()
for i in range(3):
    print q.get()
'''
'''
q = Queue.PriorityQueue()
q.put('w')
q.put(10)
q.put('A')
q.put('$')

for i in range(3):
    print q.get()
'''

#q = Queue.Queue(5)
'''
for i in range(10):
    print q.empty()
    q.put(i)
    #print q.full()
'''
#print help(q.get)

'''
import Queue,time,threading,random

class Mythread(threading.Thread):
    def __init__(self,q,worktype):
        self.jobq = q
        self.worktype = worktype
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.jobq.qsize() > 0:
                job = self.jobq.get()
                worktype = self.worktype
                self.process_job(job,worktype)
            else:
                break
    def process_job(self,job,worktype):
        self.dojob(job)

    def dojob(self,job):
        time.sleep(random.random() * 3)
        print 'doing:',job

if __name__ == '__main__':
    print 'begin...'
    q = Queue.Queue()
    num_workers = 3
    for i in range(num_workers * 2):
        q.put(i)
    for j in range(num_workers):
        Mythread(q,j).start()
             
#import aaa
'''
