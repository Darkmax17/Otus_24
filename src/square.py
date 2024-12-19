from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Сторона должна быть положительной")
        super().__init__(side, side)

        @property
        def area(self):
            return self.a * self.a

        @property
        def perimeter(self):
            return 2 * (self.a + self.a)