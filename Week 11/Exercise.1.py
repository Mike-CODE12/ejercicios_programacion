#1. Cree una clase de `Circle` con:
#    1. Un atributo de `radius` (radio).
#    2. Un método de `get_area` que retorne su área.

import math

#Option 3 (using a constructor)

class Circle():
    def __init__(self, radius):
        self.radius=radius

    def get_area(self):
        self.area=math.pi *self.radius**2
        return(self.area)

circle_1=Circle(25)
print(circle_1.get_area())

#Option1
# class Circle():
#     def get_area(self):
#         self.radius=25
#         self.area=math.pi *self.radius**2
#         return(self.area)

# circle_1=Circle()
# print(circle_1.get_area())


# class Circle():
#     def get_area(self, radius):
#         self.radius=radius
#         self.area=math.pi *self.radius**2
#         return(self.area)

# circle_1=Circle()
# print(circle_1.get_area(25))
