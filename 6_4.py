d = {
    95: 'Adam',
    85: 'Lisa',
    59: 'Bart',
}
d[72] = 'Paul'
print d
for key in d:
    print 'key' + ':' , d.get(key)