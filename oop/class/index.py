# first program with class

class dog:

    type = "mammal"
    breed = "sheperd"

    def ha(x):
        print("Dog is a", x.type)
        print("Its breed is", x.breed)

a = dog()

print(a.type)
a.ha()