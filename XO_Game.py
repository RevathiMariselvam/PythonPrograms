lst=[]


print("Player 1 should give \"x\"")
print("Player 2 should give \"o\"")
print("\n")

for i in range(0,3):
    lst.append([])
    for j in range(0,3):
        x=str(i)+str(j)
        lst[i].append(x)

for i in range(0,3):
    for j in range(0,3):
        print(lst[i][j],end="  ")
    print("\n")

count=0
while(count<=9):
                
#####Player 1
    print("Now Player 1 chance")
    place=input("Enter the postion of \"x\" for Player 1: ")
    if ((lst[int(place[0])][int(place[1])]!="x") and (lst[int(place[0])][int(place[1])]!="o")):
        lst[int(place[0])][int(place[1])]="x"
    else:
        place=input("Position occupied, Enter another position: ")
        lst[int(place[0])][int(place[1])]="x"
    for i in range(0,3):
        for j in range(0,3):
            print(lst[i][j],end="  ")
        print("\n")
    if((lst[0][0]=="x" and lst[0][1]=="x" and lst[0][2]=="x") or (lst[0][0]=="x" and lst[1][1]=="x" and lst[2][2]=="x") or (lst[1][0]=="x" and lst[1][1]=="x" and lst[1][2]=="x") or (lst[2][0]=="x" and lst[2][1]=="x" and lst[2][2]=="x") or (lst[0][0]=="x" and lst[1][0]=="x" and lst[2][0]=="x") or (lst[0][1]=="x" and lst[1][1]=="x" and lst[2][1]=="x") or (lst[0][2]=="x" and lst[1][2]=="x" and lst[2][2]=="x")):
        print("Game Over")
        break

#####Player 2
    print("Now Player 2 chance")
    place=input("Enter the position of \"o\" for Player 2: ")
    if ((lst[int(place[0])][int(place[1])]!="x") and (lst[int(place[0])][int(place[1])]!="0")):
        lst[int(place[0])][int(place[1])]="o"
    else:
        place=input("Position occupied, Enter another position: ")
        lst[int(place[0])][int(place[1])]="o"
    for i in range(0,3):
        for j in range(0,3):
            print(lst[i][j],end="  ")
        print("\n")
    if((lst[0][0]=="o" and lst[0][1]=="o" and lst[0][2]=="o") or (lst[0][0]=="o" and lst[1][1]=="o" and lst[2][2]=="o") or (lst[1][0]=="o" and lst[1][1]=="o" and lst[1][2]=="o") or (lst[2][0]=="o" and lst[2][1]=="o" and lst[2][2]=="o") or (lst[0][0]=="o" and lst[1][0]=="o" and lst[2][0]=="o") or (lst[0][1]=="o" and lst[1][1]=="o" and lst[2][1]=="o") or (lst[0][2]=="o" and lst[1][2]=="o" and lst[2][2]=="o")):
        print("Game Over")
        break
count+=1
