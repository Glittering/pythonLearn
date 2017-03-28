#coding:gbk

'''
if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print '%s,%d' % (m,person[m])
'''
'''
if __name__ == '__main__':
    person = {"li":18,"wang":50,"zhang":20,"sun":22}
    person_list = person.items()
    person_list.sort(key = lambda x:x[-1])
    the_man,age = person_list[-1]
    print the_man,':',age
'''     
        

import Queue,threading
#python 队列
    #队列模式
        #先进先出  Queue.Queue(maxsize)
        #先进后出  Queue.LifoQueue(maxsize)
        #优先级别低的先出 Queue.PriorityQueue(maxsize)

q1 = Queue.Queue()
'''
for i in range(1,11):
    q1.put(i)

while True:
    print q1.get()
    print q1.empty()
'''
'''
q2 = Queue.LifoQueue()
for i in range(1,11):
    q2.put(i)

while True:
    print q2.get()
    
'''
q3 = Queue.PriorityQueue()
'''
for i in ['W',15,'D','%','a',35,'w',55,'@',70,'N']:
    q3.put(i)

while True:
    print q3.get()
'''
'''
q1 = Queue.Queue(6)

for i in range(1,5):
    q1.put(i)
    print q1.full()
    

print q1.qsize()
'''


import Queue,threading,time,random

q = Queue.Queue(0)
num_workers = 3

class Mythread(threading.Thread):
    def __init__(self,queue,worktype):
        self.jobq = queue
        self.worktype = worktype
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.jobq.qsize() > 0:
                jobq = self.jobq.get()
                worktype = self.worktype
                self.process_job(jobq,worktype)
            else:
                break
    def process_job(self,job,worktype):
        dojob(job)

def dojob(job):
    time.sleep(random.random() * 3)
    print 'doing',job

if __name__ == "__main__":
    print 'begining...'
    for i in range(num_workers * 2):
        q.put(i)
    
    print "jobq'size:",q.qsize()

    for i in range(num_workers):
        Mythread(q,i).start()

