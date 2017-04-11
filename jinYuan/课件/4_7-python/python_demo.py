#coding:gbk

import threading,time,re

start_time = time.time()
f = open('C:\Users\guozheng\Desktop\chat\data.txt','r')
allchars = f.read()
step = len(allchars) / 10
regix = re.compile(r'\d{11}')

def find_phone_number(regix,start,stop):
    print len(re.findall(regix,allchars[start:stop + 1]))

threads = []  
for i in range(10):
    start = i * step
    stop = start + step
    
    t = threading.Thread(target = find_phone_number,args = (regix,start,stop))
    threads.append(t)

for i in range(10):
    threads[i].start()

for i in range(10):
    threads[i].join()
    
stop_time = time.time()

total_time = stop_time - start_time
print '总用时：',total_time
