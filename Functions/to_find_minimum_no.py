class Integer:
    main=[]
    def readInteger(self):
        self.value=int(input("Enter how many element need to add in the list: "))
        return self.value

    def readElements(self,value):
        lst=[]
        print("Enter the element to be added in the list: ")
        for i in range(value):
            lst.append(int(input()))
        self.main=lst
        return(self.main)

    def findMin(self,main):
        return(min(main))

obj=Integer()
x=obj.readInteger()
y=obj.readElements(x)
print("Now the list is:",y)
z=obj.findMin(y)
print("Mininmum value in the given list:",z)
