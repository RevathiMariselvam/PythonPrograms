even=0
odd=0
for i in range(12,38,1):
    if(i%2==0):
        even+=i
    else:
        odd+=i
print("Sum of Even numbers between 2 and 37: ",even)
print("Sum of Odd numbers between 2 and 37: ",odd)
