class Student:
    def __init__(self,name,roll,deg):
        self._name=name
        self._roll=roll
        self._deg=deg
    def display(self):
        print(self._name,self._roll,self._deg)

obj=Student("Revathi",35,"B.Tech")
obj.display()
