num=int(input("Enter the number to check whether it is prime number or not: "))
for i in range(2,num,1):
    if(num%i==0):
        print(f"{num} is not a prime number")
        break
    elif(num%i!=0):
        if(num==i+1):
           print(f"{num} is prime number")
##        else:
##            pass
