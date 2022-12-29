class Animal:
    def kind(self):
        print("Mammal")

class Dog(Animal):
    def breed(self):
        print("Dog is a ")

object = Dog()
object.breed()
object.kind()