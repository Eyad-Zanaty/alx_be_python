from math import pi
class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        raise NotImplementedError("Reminde that this method is expected to be overridden in any subclass of Shape")
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length= length
        self.width= width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius= radius
    def area(self):
        return pi * self.radius * self.radius