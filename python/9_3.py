d = {'adam': 95, 'lisa':85, 'bart':59, 'paul':74}

sum = 0.0
for x in d.values():
    sum += x
print sum / len(d)
