# -*- coding: utf-8 -*-
class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90: return u'A-优秀'
        elif self.__score >= 60: return u'B-及格'
        else: return u'C-不及格三档'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()
