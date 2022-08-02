km=int(input("Enter the KM covered: "))
##km-=10
##print(km)
##km-=90
##print(km)
##km*=9
##km=km+110+900
##print(km)

if(km<=10):
    money=km*11
    print(f"Total Money: {money}")
elif(km<90):
    km-=10
    money=(km*10)+110
    print(f"Total Money: {money}")
elif(km>90):
    km-=100
    money=(km*9)+110+900
    print(f"Total Money: {money}")
