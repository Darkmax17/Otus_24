class Figure:
    @property
    def area(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    @property
    def perimeter(self):
        raise NotImplementedError("Этот метод должен быть переопределен в подклассе")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Переданный объект должен быть геометрической фигурой")
        return self.area + figure.area
