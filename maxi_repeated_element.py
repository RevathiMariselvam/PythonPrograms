lst=[1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]

rep={}
for i in lst:
    x=lst.count(i)
    if(x>1):
        rep.update({i:x})
print(rep)

value=[]
for i in rep.values():
    value.append(i)

for i in range(0,len(value)):
    for j in range(i+1,len(value)):
        if(value[i]<value[j]):
            value[i],value[j]=value[j],value[i]

for i in rep:
    if(rep[i]==value[0]):
        print("Maximum repeated Element is:",i)
