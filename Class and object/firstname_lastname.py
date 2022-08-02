class Person:
    def __init__(self,firstName,lastName,age):
        self.__firstName=firstName
        self.__lastName=lastName
        self.__age=age
    def getFirstname(self):
        return(self.__firstName)
    def getLastName(self):
        return(self.__lastName)
    def getAge(self):
        return(self.__age)
    def setfirstName(self,firstName):
        self.__firstName=firstName
        print("First Name:",self.__firstName)
    def setlastName(self,lastName):
        self.__lastName=lastName
        print("Last Name:",self.__lastName)
    def setage(self,age):
        if(age<=0 or age>100):
            self.__age=0
        else:
            self.__age=age
    def fullName(self):
        return(self.__firstName+" "+self.__lastName)
    def Teen(self):
        if(self.__age>=12 and self.__age<=20):
            return True
        else:
            return False
        
P1=Person("Revathi","Mariselvam",15)
print("First Name: ",P1.getFirstname())
print("Last Name: ",P1.getLastName())
print("Full Name:",P1.fullName())
print("Age:",P1.getAge())
P1.Teen()
print("Teen or Not:",P1.Teen())
P1.setfirstName("Gayathri")
P1.setlastName("Subramanium")
P1.setage(102)
print("Full Name:",P1.fullName())
print("Age:",P1.getAge())
P1.Teen()
print("Teen or Not:",P1.Teen())
