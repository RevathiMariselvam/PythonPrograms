N=int(input("Enter the No. of Tickets: "))
lst=[]
dic={}
print("Enter the Ticket Number and Time slot:(Format: Ticket_Number Time_Slot):\n")
for i in range(0,N):
    str=input()
    x=str.split(" ")
    lst.append(x)

temp=[]
for i in range(0,len(lst)):
    temp.append([])
    for j in range(0,len(lst[i])):
        temp[i].append(int(lst[i][j]))

for i in range(0,len(lst)):
    for j in range(0,len(lst)):
        if(lst[i][1]<lst[j][1]):
            lst[i],lst[j]=lst[j],lst[i]

for i in range(0,len(lst)-1):
    if(lst[i][1]==lst[i+1][1]):
        if(lst[i][0]>lst[i+1][1]):
            lst[i],lst[i+1]=lst[i+1],lst[i]

print("Ticket Number Order: ",end=" ")
for i in range(0,len(lst)):
    print(lst[i][0],end=" ")
        
