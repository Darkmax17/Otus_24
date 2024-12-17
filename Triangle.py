import math

class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

class Square:
    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4

t = Triangle(10, 15, 20)
s = Square(5)

total_area = t.area + s.area
total_perimeter = t.perimeter + s.perimeter
