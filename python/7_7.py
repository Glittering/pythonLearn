def average(*args):
    sum = 0
    for x in args:
        sum += x
    if sum:
        return sum / len(args)
    else:
        return None

print average()
print average(1, 2)
print average(1, 2, 4, 6)

