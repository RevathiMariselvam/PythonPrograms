def hasSharedDigit(x,y):
    if((x>=10 and y<=99) and ((x%10)==(y//10) or (x%10)==(y%10) or (x//10)==(y%10) or (x//10)==(y//10))):
        return True      
    else:
        return False

x=int(input("Enter the Value of x: "))
y=int(input("Enter the Value of y: "))

result=hasSharedDigit(x,y)
print("Result:",result)
