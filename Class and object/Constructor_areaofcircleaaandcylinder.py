import Constructors as c
import math

class Circle:
    def __init__(self,radii):
        self.radii=radii
    def getArea(self):
        return math.pi*(self.radii**2)

class Cylinder(Circle):
    def __init__(self,radii,height):
        super().__init__(radii)
        self.height=height
    def getVolume(self):
        return(math.pi*(self.radii**2)*self.height)

area=Circle(10)
volume=Cylinder(2,2)

x=volume.getVolume()
y=area.getArea()
print("Area of Circle",x)
print("Volume of Cylinder",y)

obj=c.Rectangle(2,2)
print(obj.length)
