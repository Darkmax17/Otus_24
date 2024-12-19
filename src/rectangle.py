from figure import Figure

class Rectangle(Figure):
    def __init__(self, a, b):
        if a <= 0 or b <= 0:
            raise ValueError("Длины сторон a и b должны быть положительными")
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)