l = ['adam', 'lisa', 'bart', 'paul']

for index, name in zip(l, range(1, 5)):
    print index, '-', name

for index, name in enumerate(l):
    print index+1, '-', name

