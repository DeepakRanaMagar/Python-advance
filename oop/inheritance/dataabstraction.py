# (__)underscore is used as prefix to the attribute which is to be hidden 

# need to use Python Abstract Base classes(ABCs), need to import ABCMeta and abstractmethod from abc module

from abc import ABCMeta, abstractmethod
class Shape:
    __metaclass__ = ABCMeta

    def __init__(self, shapeType):
        self.shapeType = shapeType

    @abstractmethod
    def area(self):
        pass 

    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.__init__(self, 'Rectangle')
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length*self.breadth

    def perimeter(self):
        return 2*(self.length + self.breadth)

class Circle(Shape):
    pi = 3.14

    def __init__(self, radius):
        Shape.__init__(self, 'Circle')
        self.radius = radius

    def area(self):
        return round(Circle.pi*(self.radius**2),2)
    
    def perimeter(self):
        return round(2*Circle.pi*self.radius,2)