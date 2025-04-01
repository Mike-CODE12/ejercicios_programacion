#1. Cree una clase de `Circle` con:
#    1. Un atributo de `radius` (radio).
#    2. Un método de `get_area` que retorne su área.

import math

#Option1
class Circle():
    def get_area(self):
        self.radius=25
        self.area=math.pi *self.radius**2
        return(self.area)

circle_1=Circle()
print(circle_1.get_area())


#Option 2

#class Circle():
#    def get_area(self, radius):
#        self.radius=radius
#        self.area=math.pi *self.radius**2
#        return(self.area)

#circle_1=Circle()
#print(circle_1.get_area(25))


#Option 3 (It could be with a constructor)
