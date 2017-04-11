import time

def performance(unit):
    def performance_decorator(f):
        def fn(x):
            print 'call ' + f.__name__ + 'at time ' + str(time.time()) + unit +'\n'
            return f(x)
        return fn
    return performance_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)
