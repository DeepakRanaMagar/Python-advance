class A:
    def a(self):
        return 100
class B(A):
    def a(self):
        return 200
class C(A):
    def a(self):
        return 300
obj = A()
obj1 = B()
obj2 = C()

print("Value of A: ", obj.a())
print("Value of B: ", obj1.a())
print("Value of C: ", obj2.a())

