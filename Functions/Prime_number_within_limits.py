##def prime(limit):
##    for num in range(2,limit):
##        for i in range(num-1,2,-1):
##            if(num%i==0):
##                break
##        else:
##            print(num,end=" ")
##                   
##prime(int(input("Enter the limit of Prime Number to display:")))

print()

def prime(limit):
    for num in range(2,limit):
        for i in range(num-1,2,-1):
            if(num%i==0):
                break
        else:
            print(num,end=" ")
                   
prime(int(input("Enter the limit of Prime Number to display:")))
