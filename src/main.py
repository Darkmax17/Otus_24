
from triangle import Triangle
from rectangle import Rectangle
from square import Square
from circle import Circle

square = Square(10)  
print(f"Площадь квадрата: {square.area}")

triangle = Triangle(13, 14, 15)  
print(f"Площадь треугольника: {triangle.area}")

total_area = triangle.add_area(square)
print(f"Сумма площадей треугольника и квадрата: {total_area}")

circle = Circle(5)
print(f"Площадь круга: {circle.area}")

total_area_circle_triangle = circle.add_area(triangle)
print(f"Сумма площадей круга и треугольника: {total_area_circle_triangle}")

rectangle = Rectangle(4, 6)
print(f"Площадь прямоугольника: {rectangle.area}")

total_area_rectangle_square = rectangle.add_area(square)
print(f"Сумма площадей прямоугольника и квадрата: {total_area_rectangle_square}")
