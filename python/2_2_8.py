def calc(x, y):
    return x * y
def calc_prod(list):
    def f():
        return reduce(calc, list)
    return f

h = calc_prod([1, 2, 3, 4])
print  h()
