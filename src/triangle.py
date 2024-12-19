import math
from figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть положительными")

        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        s = self.perimeter / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c