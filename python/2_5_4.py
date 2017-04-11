import json

class student(object):
    def read(self):
        return r'["Tim", "Bob", "Alice"]'


s = student()
print json.load(s)
