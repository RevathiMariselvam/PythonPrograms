##class Number:
##    def __init__(self,name):
##        self.name=name
##    def evenNumber(self,num):
##        count=0
##        while(num!=0):
##            num//=10
##            num1=num%10
##            if(num1%2==0):
##                count=count+num1
##        print("Sum of the Even numbers in the given number:",count)
##
##x=Number("suba")
##print(x.name)
##x.evenNumber(12345)
import math
class A:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
class C(A):
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b
class B(A):
    def sqrt(self,a):
        return math.sqrt(a)

b=B()

print(b.add(3,3))
print(b.mul(4,5))
print(b.sqrt(4))
print(a.sqrt(5))
