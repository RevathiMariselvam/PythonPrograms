num1=int(input("Enter the value of Number 1: "))
num2=int(input("Enter the value of Number 2: "))
operator=input("Enter the Mathematical Operations to be done (+,-,*,/): ")
if(operator=="+"):
    num3=num1+num2
    print(f"Sum of two number is: {num3}")
elif(operator=="-"):
    num3=num1-num2
    print(f"Difference of two number is: {num3}")
elif(operator=="*"):
    num3=num1*num2
    print(f"Multiplication of two number is: {num3}")
elif(operator=="/"):
    num3=num1/num2
    float(num3)
    print(f"Division of two number is: {num3}")
    
