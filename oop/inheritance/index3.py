class Person:
    def __init__(self):
        Person.__init__(self)
        print("Parent init")
    
class Student(Person):
    def __init__(self):
        print("Child Init")

obj = Student()
