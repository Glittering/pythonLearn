class Person(object):

    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count
        
    def __init__(self, name):
        self.name = name
        Person.__count = Person.__count + 1
            #Person.__count 修改类的属性。 self.__count修改 对象的属性

print Person.how_many()

p1 = Person('Bob')

print Person.how_many()
