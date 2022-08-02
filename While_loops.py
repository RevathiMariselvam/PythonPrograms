a=1
while(a<=10):
    print("No:",a,end="   ")
    print("Squares:",a**2)
    a+=1
print()

print()

num=int(input("Enter the number to check whether it is prime or not: "))
if(num%2==0):
    print(f"Given number {num} is not a prime number")
else:
    count=num
    while(num%2!=0):
        count-=1
        if(num%count!=0 and count==2):
            print(f"Given number {num} is prime number")
            break
        elif(num%count==0):
            print(f"Given number {num} is not a prime number")
            break
        else:
            continue
                 

print()

count=0
num=int(input("Enter the number to find the No. of digits: "))
a=num
while(num/10!=0):
    count+=1
    num=num//10
    if(num==0):
        print(f"Number of digits in {a} is {count}")

print()


num=int(input("Enter the Fibonnaci numbers to diplay: "))
count=2
a=0
b=1
c=0
print("Fibonacci numbers are:",end=" ")
while(count!=num):
    c=a+b
    print(a,end=" ")
    a=b
    b=c
    count+=1
    
print()
print()

a=int(input("Enter the integer: "))
n=int(input("Enter the value: "))
count=0
num=0
while(n!=num):
    count+=1
    num=a**count
    if(n==num):
        print(f"Exponent value is: {count}")
        break
    elif(n<num):
        print("Enter the correct value")
        break


print()

digits=0
num2=0
num3=0
num=int(input("Enter the number are need to be reverse: "))
num4=num
num1=num
while(num!=0):
    digits+=1
    num=num//10
    if(num==0):
        print(f"No. of digits: {digits}")
while(digits!=0):
    digits-=1
    num2=num1
    num1//=10
    num2%=10
    num2=num2*(10**digits)
    num3=num3+num2
    if(digits==0):
        print(f"Reversed number is: {num3}")
if(num3==num4):
    print(f"Number {num4} is palindrome")
else:
    print(f"Number {num4} is not palindrom")
    

print()

num2=0
num3=0
j=1
num1=int(input("Enter the number to check the strong number: "))
num4=num1
while(num1!=0):
    num2=num1
    num1//=10
    num2%=10
    j=1
    for i in range(1,num2+1):
        j=j*i
    print(f"Factorial of {num2} is {j}")
    num3=num3+j
print(f"Sum of factorial is {num3}")
if(num4==num3):
    print(f"Given number {num3} is strong number")
else:
    print(f"Given number {num4} is not strong number")

print()

num=int(input("Enter the number to check whether it is Armstrong number or not: "))
num1=num
digits=1
while(num1>10):
    digits+=1
    num1//=10
    num2=num1%10
num1=num
num3=0
while(num!=0):
    num2=num%10
    num//=10
    num3=num3+num2**digits
if(num3==num1):
    print(f"Given number {num1} is Armstrong number")
else:
    print(f"Given number {num1} is not Armstrong number")
    
