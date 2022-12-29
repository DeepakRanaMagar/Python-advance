# simple calculation with multi heritance 
# parent class 1 
class add:
    def sum(self,a,b):
        return a + b
# parent class 2 
class sub:
    def subtract(self, a,b):
        return a -b
# child class
class child(add , sub):
    def div(self, a, b):
        return a / b 

obj = child()
print(obj.sum(10,20))
print(obj.subtract(10,20))
print(obj.div(10,20))
# to check the status of parent and base class relation
print(issubclass(child, add))
print(issubclass(sub, add))
# to check the status of object and class method
print(isinstance(obj,child))
