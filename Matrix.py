lst=[]

ro=int(input("Enter the No. of Rows: "))
col=int(input("Enter the No. of Columns: "))

for i in range(0,ro):
    lst.append([])
    for j in range(0,col):
        x=int(input("Enter the element to be added in the list: "))
        lst[i].append(x)

print("Matrix: ")
for i in range(0,ro):
    for j in range(0,col):
        print(lst[i][j],end=" ")
    print()

print()

print("Transpose Matrix: ")
for  i in range(0,ro):
    for j in range(0,col):
        print(lst[j][i],end=" ")
    print()

print()

##lst1=[]
##for i in range(0,ro):
##    lst1.append([])
##    for j in range(0,col):
##        x1=int(input("Enter the element to be added in the list: "))
##        lst1[i].append(x1)

print("Addition of before printed two matrices: ")
for i in range(0,ro):
    for j in range(0,col):
        temp=lst[i][j]+lst[j][i]
        if temp<10:
            print(temp,end="  ")
        else:
            print(temp,end=" ")
    print()
    
print()
