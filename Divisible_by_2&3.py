num=int(input("Enter the number to check whether it divisible by both 2 and 3: "))
if(num%3==0 and num%2==0):
    print(f"Number {num} is divisible by both 2 and 3")
elif(num%3==0):
    print(f"Number {num} is divisible only by 3")
elif(num%2==0):
    print(f"Number {num} is divisible only by 2")
else:
    print("Number is not divisible by both 3 and 2")
