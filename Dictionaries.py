##details={"name":"Revathi","dob":25,"age":32}
##print(details["name"]
##print(details.get("dob"))
##
##details.keys()
##
##for i in details:
##    print(i)
##    print(details[i])
##x=details.items()
##print(x)
##
##for i in x:
##    print(i)
##    print(i[0],i[1])
##details.pop("name")
##details.popitem()
##print(details)
##details.update({"name":"Revathi"})
##print(details)
##
##details={"name":"Revathi","dob":25,"age":32}
##print("Dictionary:",details)
##
##print()
##
##details.update({input("Enter the New Key: "):input("Enter the New value: ")})
##print("New key and value are added:",details)
##
##print()
##
##x=input("Enter the key to check whether it already present or not: ")
##details.keys()
##lst=[]
##for i in details:
##    lst.append(i)
##print(lst)
##if x in lst:
##    print(f"{x} key is present in the Dictionaries")
##else:
##    print(f"{x} key is not present in the Dictionaries")
##
##print()
##
##details_1={"Nationality":"India","Language":"Tamil"}
##print("Another Dictionary:",details_1)
##
##for i in details_1:
##    details.update({i:details_1[i]})
##print("Now concatenated two dictionaries:",details)
##
##print()
##
##dic={1:"red",2:"green",3:"black",4:"white",5:"blue"}
##lst=[]
##for i in dic:
##    a=[i,dic[i]]
##    lst.append(a)
##print(lst)
##
##print()
##
##dic={"VI":[1,2,3],"VII":[4,5,6],"VIII":[7,8,9],"VIV":[10,11,12]}
##print("Dictionaries:",dic)
##value=[]
##key=[]
##temp=[]
##for i in dic.values():
##    value.append(i)
##for i in dic.keys():
##    key.append(i)
##
##for i in range(len(value)):
##     a=value[i]
##     temp.append([])
##     for j in range(0,len(a)):
##         if(a[j]%2==0):
##             temp[i].append(a[j])
##
##for i in range(0,len(dic)):
##    dic[key[i]]=temp[i]
##print("Filtered the even values in the given dictionaries",dic)
##
##print()
##
##word=input("Enter the string: ")
##key=[]
##value=[]
##dic={}
##
##for i in range(0,len(word)):
##    key.append(word[i])
##
##for i in key:
##    temp=key.count(i)
##    value.append(temp)
##
##for i in range(0,len(word)):
##    dic.update({key[i]:value[i]})
##print("Count of letters",dic)
##
##print()
##
##lst=[{"v":"s001"},{"v":"s002"},{"v1":"s001"},{"v1":"s005"},{"vii":"s005"},{"v":"s009"},{"viii":"s007"}]
##print("Dictionaries:",lst)
##value=[]
##for i in range(0,len(lst)):
##    for j in lst[i].values():
##        value.append(j)
##temp=[]
##for i in range(0,len(value)):
##    x=value.count(value[i])
##    if(x==1):
##       temp.append(value[i])
##print("Unique Values in the Dictionaries are:",temp)
##
##print()

##d1={"a":100,"b":200,"c":300}
##d2={"a":300,"b":200,"d":400}
##d3=d1
##for i in d2:
##    if i in d1:
##        d2[i]=d1[i]+d2[i]
##    d3.update({i:d2[i]})
##print("Combined 2 dictionaries by adding values of common key:",d3)
##
##



dic={"a":5,"b":14,"c":32,"d":35,"e":24,"f":100,"g":57,"h":8,"i":100}
x=dic.keys()
y=dic.values()
print("Dictionaries:",dic)

value=[]
for i in y:
    value.append(i)


for i in range(0,len(value)):
    for j in range(i+1,len(value)):
        if(value[i]<value[j]):
            value[i],value[j]=value[j],value[i]


print("1. To Find 1 Maximum value")
print("2. To Find 2 Maximum value")
print("3. To Find 3 Maximum value")
x=int(input("Enter the Number to find the Maximum value:"))

key=[]
count=0
for i in dic:
    if(x==1):
        if(value[0]==dic[i]):
            key.append(i)
            print("One key which holds the maximum value",key)
            break
    elif(x==2):
        if(value[0]==dic[i] or value[1]==dic[i]):
            count+=1
            key.append(i)
            if(count==2):
                print("Two key which holds the maximum value",key)
                
    elif(x==3):
        if(value[0]==dic[i] or value[1]==dic[i] or value[2]==dic[i]):
            count+=1
            key.append(i)
            if(count==3):
                print("Three key which holds the maximum value",key)
    
print()

##dic={}
##for i in range(1,26):
##    dic.update({i:""})
##
##for i in dic:
##    if(i%2==0):
##        dic[i]="football"
##    elif(i%3==0):
##        dic[i]="basketball"
##    elif(i%5==0):
##        dic[i]="cricket"
##    else:
##        dic[i]="none"
##print(dic)

        
