import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Circle):
    def __init__(self, side_a):
        super().__init__(side_a / math.sqrt(2))
        self.side_a = side_a

    @property
    def area(self):
        return self.side_a ** 2

    def add_area(self, figure):
        if not isinstance(figure, (Circle, Square)):
            raise ValueError
        return self.area + figure.area

try:
    c = Circle(5)
    s = Square(5)

    total_area = s.add_area(c)
    circle_perimeter = c.perimeter
except ValueError as e:
    pass
