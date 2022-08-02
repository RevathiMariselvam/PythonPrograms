class Mobile:
    ram=6
    camera=64
    display=6
    color="Blue"
    def cameraQuality(self):
        print("Camera quality of the mobile is 64MegaPixel")
    def charge(self):
        print("Charging speed is high")

poco=Mobile()
print(poco.ram)
poco.color="Black"
print(poco.color)
poco.cameraQuality()

oppo=Mobile()
print(oppo.color)
