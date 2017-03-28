#coding:gbk


import time,threading,re,wx,thread
'''
begin_time = time.time()

thefile = open('C:\Users\guozheng\Desktop\chat\data.txt','r')
content = thefile.read()
#print allchars/10
re_object = re.compile(r'\d{11}')
threads = []

def find_phone_number(re_object,start,stop):
    print 'the phone count:%s'%(len(re.findall(re_object,content[start:stop + 1])))

for i in range(10):
    step = len(content)/10
    start = i * step
    stop = start + step

    t = threading.Thread(target = find_phone_number,args = (re_object,start,stop))
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()

ending_time = time.time()
print 'the_total_time is:',(ending_time - begin_time)
'''

class Find_Phone_Number(threading.Thread):
    def __init__(self,strings,star,stop):
        self.strings = strings
        self.star = star
        self.stop = stop
        threading.Thread.__init__(self)

    def run(self):
        print 'the phone count:%s'%(len(re.findall(r'\d{11}',self.strings[self.star:self.stop + 1])))

def demo(document):
    thefile = open(document,'r')
    strings = thefile.read()

    threads = []
    for i in range(10):
        step = len(strings)/10
        star = i * step
        stop = star + step
        t = Find_Phone_Number(strings,star,stop)
        threads.append(t)
    #threads[0].start()

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()

if __name__ == '__main__':
    begin_time = time.time()
    '''
    thefile = open('C:\Users\guozheng\Desktop\chat\data.txt','r')
    strings = thefile.read()

    threads = []
    for i in range(10):
        step = len(strings)/10
        star = i * step
        stop = star + step
        t = Find_Phone_Number(strings,star,stop)
        threads.append(t)
    #threads[0].start()

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()
    '''
    demo('C:\Users\guozheng\Desktop\chat\data.txt')
    ending_time = time.time()
    print 'the_total_time is:',(ending_time - begin_time)

