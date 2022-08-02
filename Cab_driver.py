cab=[]
pick=[]
drop=[]
pas=[]
dist=[]
cost=[]
total_cost=0

for i in range(0,5):
    print()
    pick.append(input("Enter the Pick Up Point: "))
    drop.append(input("Enter the Drop Point: "))
    pas.append(int(input("No. of Passenger travelled: ")))
    dist.append(int(input("Distance Travelled: ")))
for i in range(0,5):
    if(pas[i]<=2 and dist[i]<=55):###Passenger less than 2 and distance is less than 55
        temp=dist[i]*10
        cost.append(int(temp))
    elif((pas[i]>2 and pas[i]<=5) and dist[i]<=55):###Passenger more than 2 and distance is less than 55
        temp=dist[i]*15
        cost.append(int(temp))
    elif(dist[i]>55 and pas[i]<=2):###Passenger less than 2 and distance is more than 55
        temp=10+(10*(60/100))*dist[i]
        cost.append(int(temp))
    elif(dist[i]>55 and pas[i]<=5 and pas[i]>2):###Passenger more than 2 and distance is more than 55
        temp=15+(15*(60/100))*dist[i]
        cost.append(int(temp))
    elif(pas[i]>5 or dist[i]<=0):
        print("Enter the passenger should not be more than 5 and Distance travelled should not be 0 or less than 0")


for i in range(0,len(cost)):
    total_cost=total_cost+cost[i]

print("")
cab=[]
for i in range(0,5):
    a={"Cab Duty":i+1,"Pick Up Point":pick[i],"Drop Point":drop[i],"No.of Passenger":pas[i],"Distance Travelled":dist[i],"Cost":cost[i]}
    cab.append(a)
print("Cab Driver Database:",cab)

print("")
print("Total Money earned by the cab driver today:",total_cost)
