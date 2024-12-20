class Square:
    def __init__(self, side_a):
        self.side_a = side_a

    @property
    def area(self):
        return self.side_a ** 2

    @property
    def perimeter(self):
        return self.side_a * 4

class Rectangle(Square):
    def __init__(self, side_a, side_b):
        super().__init__(side_a)
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def add_area(self, figure):
        if not isinstance(figure, Square):
            raise TypeError("Argument figure must be a class Square or child class")
        return self.area + figure.area

s = Square(10)
r = Rectangle(3, 5)

total_area = s.area + r.area
total_perimeter = s.perimeter + r.perimeter