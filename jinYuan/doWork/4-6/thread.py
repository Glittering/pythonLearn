import thread, threading
from time import ctime, sleep

def loop0():
    print ('start loop0 at:',ctime())
    sleep(2)
    print ('loop0 done at:',ctime())


def loop1():
    print ('start loop1 at:',ctime())
    sleep(3)
    print ('loop1 done at:',ctime())


def main():
    print ('starting all at:',ctime())
    # loop0()
    # loop1()
    thread.start_new_thread(loop0,(),)
    thread.start_new_thread(loop1,(),)
    print ('all done at:',ctime())


main()
