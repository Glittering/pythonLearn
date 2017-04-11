#coding:gbk

import time

class OurReader():
    def __init__(self,path):
        self.f = open(path,'r')
        self.f.seek(0,2)
        self.file_size = self.f.tell()
        self.f.seek(0,0)

    def one_page(self):
        #print self.f.read(800)
        for i in range(10):
            print self.f.readline(),
        self.page_num = self.f.tell()
        print '您已阅读%.3f%%'%((self.page_num / float(self.file_size)) * 100)
    '''
    def auto(self):
        self.one_page()

    def manual(self):
        self.one_page()
    '''
    def __del__(self):
        self.f.close()

if __name__ == '__main__':
    reader = OurReader('1.txt')
    while True:
        enter = raw_input("请输入'auto' 或者 'manual':")
        if enter == 'manual':
            reader.one_page()
        elif enter == 'auto':
            while True:
                reader.one_page()
                time.sleep(3)
        elif enter == 'exit':
            break
    #reader.f.close()
    del reader
        
    

'''
reader = OurReader('1.txt')
while True:
    a = raw_input('Please Enter:')
    if a == 'auto':
        reader.auto()
    if a == 'manual':
        reader.manual()
    if a == 'exit':
        break
'''
