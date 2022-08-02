def prime(num):
    factors=[]
    if(num<=1):
        return(-1)
    for i in prime_list:
        if(num%i==0):
            factors.append(i)
    return(factors[-1])


num=int(input("Enter the Number to find the Prime factors: "))
prime_list=[]
for i in range(2, 101):
        if (i==0) or (i==1):
            continue
        else:
            for j in range(2, int(i/2)+1):
                if (i%j==0):
                    break
            else:
                prime_list.append(i)


x=prime(num)
print("Prime factor of the given number is:",x)
