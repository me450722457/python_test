from class1 import Human


class Student(Human):
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def get_school(self):
        print(self.school)

a= str(input('input your name'))
student1 = Student('长安中学', a, 16)
student1.get_age()
student1.get_name()
