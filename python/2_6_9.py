class Fib(object):
    def __init__(self):
        pass
    def __call__(self,x):
        a1 = 0
	a2 = 1
	k  = 0
	f  = [0, 1, ]
	while(k < x-2):
	    a2 = a1 + a2
	    a1 = a2 - a1
	    k += 1
	    f.append(a2)
	return f
f = Fib()
print f(10)
