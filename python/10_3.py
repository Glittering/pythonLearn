def touppers(l):
    return [x.upper() for x in l if isinstance(x,str)]

print touppers(['hello', 'world',101])
