import random
num=0
count=0
while(num!=2 and count<=5):
    rand=int(input("Enter the Number from 1-10:"))
    num=random.randint(1,10)
    count+=1
    if(rand==num):
        print("You win")
        break
    elif(count==5):
        print("You lose")
        break
