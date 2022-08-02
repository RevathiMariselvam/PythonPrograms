num=int(input("Enter the number to display the spell out: "))
spell=["zero","one","two","three","four","five","six","seven","eight","nine"]
lst=[]
while(num!=0):
    num1=num%10
    num=num//10   
    lst.append(spell[num1])
    
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")
    
    

