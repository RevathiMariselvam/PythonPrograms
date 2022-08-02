for i in range(5):
    for j in range(5):
        if(i==j or i>=j):
            print("*",end=" ")
    print()

print()

for i in range(5):
    for j in range(5):
        if(i==j or i>=j):
            print(i+1,end=" ")
    print()

print()

for i in range(6):
    for j in range(1,6):
        if(i==j or i>=j):
            print(j,end=" ")
    print()


print()

for i in range(1,6):
    for j in range(1,6):
        if(i==j or i>=j):
            print(j*2,end=" ")
    print()

print()


for i in range(1,6):
    for j in range(1,6):
        if(i==j or i>=j):
            if(i*2<=9):
                print(i*2,end="  ",)
            else:
                print(i*2,end=" ")
    print()

print()



for i in range(1,10,2):
    for j in range(1,10,2):
        if(i==j or i>=j):
            print(i,end="  ",)
    print()

print()


for i in range(1,10,2):
    for j in range(1,10,2):
        if(i==j or i>=j):
            print(j,end="  ",)
    print()

print()

c=0
for i in range(5):
    for j in range(5):
        if(i==j or i>=j):
            c+=1
            if(c<10):
                print(f"{c} ",end="  ")
            elif(c>=10):
                print(c,end="  ")
    print()
