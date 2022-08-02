class Laptop:
    size=25
    ram=5
    rom=10
    color="black"
    def videoCall(self,a):
        size=a
        print("video call is on",size)
    def openPython(self):
        print("python program ")
    def calculation(self):
        print("calculator is opened")

lap1=Laptop()
##print(lap1.size)
##lap1.size=30
##print(lap1.size)
##print(lap1.ram)
##print(lap1.rom)
##print(lap1.color)
lap1.videoCall(45)
print(lap1.size)
##lap1.openPython()
##lap1.calculation()
##lap2=Laptop()
##print("lap2.size",lap2.size)
