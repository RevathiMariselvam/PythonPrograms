##class Employee:
##    def __init__(self):
##        self.name="john"
##        self.age=27
##        self.salary=10000
##    def __init__(self,name,age,salary):
##        self.name=name
##        self.age=age
##        self.salary=salary
##john=Employee("jack",25,15000)
##print(john.name)
##print(john.age)
##print(john.salary)

##john.setValue("john",27,10000)

class Phone:
    def __init__(self,name,brand,price):
        self.name=name
        self.brand=brand
        self.price=price
    def call(self):
        print("you can make a call in ",self.name)
class Mobile(Phone):
    
    def __init__(self,name,brand,price,ram,battery):
        super().__init__(name,brand,price)
        self.ram=ram
        self.battery=battery
    def calculator(self):
        print("you can perform any mathematical operation")
    def camera(self):
        super().call()
        print("you can take photo")

vivo=Mobile("vivo","S22",20000,6,5000)
##vivo.call()
vivo.camera()







    
