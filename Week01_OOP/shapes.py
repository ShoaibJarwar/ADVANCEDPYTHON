import math


class Shape:
    def area(self):
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def __str__(self):
        return f"The Circle with radius {self.radius} has area: {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"The Rectangle with width {self.width} and height {self.height} has area: {self.area():.2f}"
