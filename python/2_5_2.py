class person(object):
    def __init__(self, name, gender):
        self.name = name
	self.gender = gender

class teacher(person):
    def __init__(self, name, gender,course):
        super(teacher, self).__init__(name, gender)
	self.course = course
t = teacher('alice', 'female', 'english')
print t.name
print t.course
