import time

def performance(f):
    def fn(x):
        print 'call ' + f.__name__ + 'at time ' + str(time.time()) + '\n'
        return f(x)
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)
