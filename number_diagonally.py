
for i in range(0,7,1):
    for j in range(0,7,1):
        if(i==j or i>=j):
            c=i*j
            if(c<9):
                print(c,end="  ")
            else:
                print(c,end=" ")
        
    print()

print()

b=1
for i in range(0,4):
    for j in range(0,4):
        if(j==0):
            b+=(i*2)
            print(b,end=" ")
        elif(i>=j):
            b-=1
            print(b,end=" ")
    print()

print()

for i in range(0,5,1):
    for j in range(0,5,1):
        if(j==0):
            b=10
            print(b,end=" ")
        elif(i>=j):
            b-=2
            print(b,end=" ")
    print()

print()

for i in range(0,5,1):
    for j in range(0,5):
        if(i==j or i>=j):
            a=i-j+1
            print(a,end=" ")
    print()

print()

a=0
b=0
for i in range(0,3):
    for j in range(0,a+1):
        if(i==j or i>=j):
            b+=1
            print(b,end=" ")
        else:
            b+=1
            print(b,end=" ")
    a+=2
    print()
    
print()

a=0
b=0
for i in range(0,5):
    for j in range(0,a+1):       
        if(i==j or i>=j):
            b+=1
            print(b,end=" ")
        else:
            b-=1
            print(b,end=" ")
    b=0        
    a+=2
    print()









