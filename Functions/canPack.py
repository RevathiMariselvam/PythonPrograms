def canPack(bigcount,smallcount,goal):
    total=bigcount+smallcount
    goal_temp=(bigcount*5)+(smallcount*1)
    if(bigcount<0 or smallcount<0 or goal<0):
        return(False)
    elif(goal_temp>=goal):
        return True
    else:
        return False



bigcount=int(input("Enter the Big Count value: "))
smallcount=int(input("Enter the Small Count value: "))
goal=int(input("Enter the Goal value: "))

result=canPack(bigcount,smallcount,goal)
print(result)
