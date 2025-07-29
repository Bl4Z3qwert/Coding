import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 2)

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

circle = Circle(7)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())




