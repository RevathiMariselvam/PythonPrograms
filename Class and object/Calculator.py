class SimpleCalc:
    __firstNum=20
    __secNum=2
    def getfirstNum(self):
        return(self.__firstNum)
    def getsecNum(self):
        return(self.__secNum)
    def setfirstNum(self,firstNum):
        self.__firstNum=firstNum
    def setsecNum(self,secNum):
        self.__secNum=secNum
    def addition(self):
        return(self.__firstNum+self.__secNum)
    def subtraction(self):
        return(self.__firstNum-self.__secNum)
    def multiplication(self):
        return(self.__firstNum*self.__secNum)
    def division(self):
        return(self.__firstNum/self.__secNum)

calc=SimpleCalc()
calc.setfirstNum(10)
calc.setsecNum(5)
print("Addition:",calc.addition())
print("Subtraction:",calc.subtraction())
print("Multiplication:",calc.multiplication())
print("Division:",calc.division())
