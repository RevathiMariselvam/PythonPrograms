##n=int(input("Enter the number of rows and column: "))
##
##print()
##
##for i in range(0,n):
##    for j in range(0,n):
##        print("*",end=" ")
##    print()
##
##print()
##
##for i in range(0,n):
##    for j in range(0,i+1):
##        print("*",end=" ")
##    print()
##
##print()
##
##
##for i in range(0,n):
##    for j in range(i,n):
##        print("*",end=" ")
##    print()
##
##print()
##
##for i in range(0,n):
##    for j in range(1,i+1):
##        print(" ",end=" ")
##    for j in range(i,n):
##        print("*",end=" ")
##    print()
##
##print()
##
##for i in range(0,n):
##    for j in range(i,n-1):
##        print(" ",end=" ")
##    for j in range(0,i+1):
##        print("*",end=" ")
##    print()
##
##print()
##
##
##for i in range(0,n+1):
##    for j in range(0,i*2):
##        print("*",end=" ")
##    print()

for i in range(0,5):
    for j in range(0,5):
        if(i==3 or ((j==0) and (i>1)) or ((j==4) and (i>1)) or ((j==1) and (i%2!=0)) or (j==3) and(i%2!=0) or ((i==0) and (j==2))):
           print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
