class Fib(object):

    def __init__(self, num):
        self.s = [0 , 1]
        a1 = 0
        a2 = 1
        k  = 0
        while(k < num-2):
            a2 = a1 + a2
            a1 = a2 - a1
            self.s.append(a2)
            k += 1

    def __len__(self):
        return len(self.s)
        
    def __str__(self):
        return str(self.s)

f = Fib(10)
print f
print len(f)
