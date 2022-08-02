def isValid(x):
    if(x>=10 and x<=1000):
        return True
    else:
        return False

def hasSameLastDigit(x,y,z):
    if((isValid(x) and isValid(y) and isValid(z)) and ((x%10)==(y%10) or (x%10)==(z%10) or (y%10)==(z%10))):
        return True
    else:
        return False
       

x=int(input("Enter the value of x: "))
y=int(input("Enter the value of y: "))
z=int(input("Enter the value of z: "))
a=isValid(x)
print("isValid Function:",a)
b=hasSameLastDigit(x,y,z)
print("hasSameLastDigit",b)

