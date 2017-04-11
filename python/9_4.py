d = {'adam':95, 'lisa':85, 'bart':59, 'paul':74}

sum = 0.0
for k,v in d.items():
    sum += v
    print k, ':', v
print 'average', ':', sum /len(d)
