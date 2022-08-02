##tup=(2,5,6,7)
##tup1=(8,9,10,11)
##lst=list(tup)
##print(lst)
##lst1=tup+tup1
##print(lst1)

print()

tup=[("item1","12.20"),("item2","15.10"),("item3","24.5")]
temp=[]
lst=[]
m=0
for i in tup:
    x=list(i)
    temp.append([x[0],float(x[1])])

for i in range(0,len(temp)):
    for j in range(i+1,len(temp)):
        if temp[i][1]<temp[j][1]:
            temp[i],temp[j]=temp[j],temp[i]        

for i in range(0,len(temp)):
    temp[i][1]=str(temp[i][1])

for i in temp:
    lst.append(tuple(i))
print("Float value is sorted:",lst)


##print()
##
##a=(1,2,3,5,5,6,3,2,1)
##b=list(a)
##for i in b:
##    x=b.count(i)
##    if(x>1):
##        print("")
##        
##
##
##
##
##
##
