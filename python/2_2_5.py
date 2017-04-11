def prod(x, y):
    return x * y

print reduce(prod, [2, 4, 5, 7, 12])

def prod2(*x):
    sum = 1
    for y in x:
        sum *= y
    return sum
print prod2(1, 2, 3)
