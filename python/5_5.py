sum = 0
x = 1
while x <= 100:
    y = 2
    while y < x:
        if x % y == 0:
             break
        else:
             y += 1
    if y == x:
        print x
        sum += x
    x = x + 1
print sum
