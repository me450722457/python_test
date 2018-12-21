class Students():
    name = 'bbb'
    age = 20
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age
        self.__class__.sum += 1
        print(self.__age)


student1 = Students('aaa', 12)
student1._Students__age = -1
print(student1.__dict__)
print(student1._Students__age)
