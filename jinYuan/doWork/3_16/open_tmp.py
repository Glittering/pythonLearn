#!/ust/lib/python3
#coding:utf-8
import time


def isExists():
    file = raw_input('Write A FileName:')
    try:
        file = '/tmp/'+file
        with open(file,'r'):
            print 'File_Name exists.'
            isExists()
    except:
        with open(file,'w') as create_file:
            times =  time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
            create_file.write(times)
            print 'no file and touch {} \nwith {}'.format(file,times)
            isExists()

isExists()
# print time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time()))
