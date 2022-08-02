class lastDigit:
    def isValid(self,num):
        if(num>=10 and num<=1000):
            return True
        else:
            return False
    def sameLastDigit(self,a,b,c):
        if((self.isValid(a)==True) and (self.isValid(b)==True) and (self.isValid(c)==True)):
            if(a%10==b%10 or b%10==c%10 or c%10==a%10):
                return True
            else:
                return False
        else:
            return False

num=lastDigit()
x=num.sameLastDigit(41,22,71)
print(x)
y=num.sameLastDigit(9,99,999)
print(y)
