class person(object):
    def __init__(self, name, gender):
        self.name = name
	self.gender = gender

class student(person):
    def __init__(self, name, gender,score):
        super(teacher, self).__init__(name, gender)
	self.score = score

class teacher(person):
    def __init__(self, name, gender,course):
        super(teacher, self).__init__(name, gender)
	self.course = course
t = teacher('alice', 'female', 'english')

print 't is person:', isinstance(t,person)
print 't is student:', isinstance(t,student)
print 't is teacher:', isinstance(t,teacher)
print 't is boject:', isinstance(t,object)
