# 2. Cree una clase abstracta de `Shape` que:
#     1. Tenga los métodos abstractos de `calculate_perimeter` y `calculate_area`.
#     2. Ahora cree las siguientes clases que hereden de `Shape` e implementen esos métodos: `Circle`, `Square` y `Rectangle`.
#     3. Cada una de estas necesita los atributos respectivos para poder calcular el área y el perímetro.

import math

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass


    @abstractmethod  
    def calculate_area(self):
        pass


class Square(Shape):

    def __init__(self, side):
        self.side=side


    def calculate_perimeter(self):
        return self.side*4
    

    def calculate_area(self):
        return self.side*self.side


class Circle(Shape):

    def __init__(self, radius):
        self.radius=radius

    def calculate_perimeter(self):
        return math.pi*2*self.radius
    

    def calculate_area(self):
        return math.pi*self.radius**2


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length=length
        self.width=width


    def calculate_perimeter(self):
        return 2*(self.length+self.width)
    

    def calculate_area(self):
        return self.length*self.width    
    

circle=Circle(7)
square=Square(7)
rectangle=Rectangle(7, 7)
print(circle.calculate_area())
print(circle.calculate_perimeter())
print(square.calculate_area())
print(square.calculate_perimeter())
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())