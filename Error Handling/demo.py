##try:
##    a=int(input("enter a number"))
##except:
##    print("Error occurred")
##else:
##    print(a)
##print("program ends")


try:
    a=int(input("Enter the Value of A: "))
    b=int(input("Enter the Value of B: "))
    if(b==2):
        raise ZeroDivisionError
    else:
        c=a//b
except ZeroDivisionError:
    print("Value should not be 0")
except:
    print("Enter only the Integer value")
else:
    print(c)
finally:
    print("Programs Ends")
