def mult(limit):
    count=0
    for i in range(1,limit+1):
        if(i%3==0 or i%5==0):
            print(i,end=" ")
            count+=i
    return count


sum=mult(int(input("Enter the Limit to find the multiple of 3 and 5:")))
print("\nSum of the Number which are divisible by 3 and 5:",sum)
