row=int(input("Enter the Odd number for Rows:"))+1
col=row-2
mid=((row-2)/2)+1


print("A in Star Pattern")
for i in range(1,row):
    for j in range(1,col):
        if(i==mid or (j==1 and i!=1) or (j==col-1 and i!=1) or (i==1 and j!=1 and j!=col-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            
print()

print("B in Star Pattern")
for i in range(1,row):
    for j in range(1,col):
        if((i==mid and j!=col-1) or (i==1 and j!=col-1) or (j==1) or (i==1 and (j!=col-1)) or (i==row-1 and j!=col-1) or (j==col-1 and i!=1 and i!=row-1 and i!=mid)):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

print()

print("L in Star Pattern")

for i in range(1,row):
    for j in range(1,col):
        if(j==1 or i==row-1):
            print("*",end=" ")
    print()

print()

print("O in Star Pattern")

for i in range(1,row):
    for j in range(1,col):
        if((i==1 and j!=1 and j!=col-1) or (j==1 and i!=row-1 and i!=1) or (i==row-1 and j!=1 and j!=col-1) or (j==col-1 and i!=row-1 and i!=1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

print("G in Star Pattern")

for i in range(1,row):
    for j in range(1,col):
        if((i==1 and j!=1 and j!=col-1) or (j==1 and i!=row-1 and i!=1) or (i==row-1 and j!=1 and j!=col-1) or (j==col-1 and i!=row-1 and i!=mid-1 and i!=1) or (i==mid and j!=1 and j!=2 and j!=3)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()


print("I in Star Pattern")

for i in range(1,row):
    for j in range(1,col):
        if((i==1) or (i==row-1) or (j==(col//2))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print()

print("N in Star Pattern")

for i in range(1,row):
    for j in range(1,row):
        if(j==1 or j==row-1 or (i==j)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
