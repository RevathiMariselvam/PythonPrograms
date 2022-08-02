import math

class Rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        print("Area of Rectangle:",(self.length)*(self.breath))

class Circle:
    def __init__(self,radii):
        self.radii=radii
    def area(self):
        print("Area of Circle: ",math.pi*(self.radii**2))

class Cylinder(Rectangle):
    def __init__(self,length,breath,height):
        super().__init__(length,breath)
        self.height=height
    def area_of_c(self):
        print("Area of Cylinder: ",self.length*self.breath*self.height)

result=Cylinder(2,2,2)
result.area_of_c()
