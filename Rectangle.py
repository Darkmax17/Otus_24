class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

    def add_area(self, figure):
        if not isinstance(figure, Rectangle):
            raise TypeError("Argument figure must be a class Rectangle or child class")
        return self.area + figure.area


class Square(Rectangle):
    def __init__(self, side_a):
        super().__init__(side_a, side_a)

r = Rectangle(3, 5)
s = Square(5)

total_area = r.area + s.area
total_perimeter = r.perimeter + s.perimeter
