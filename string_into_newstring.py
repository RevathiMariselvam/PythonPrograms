str="ab2bc4def5"

temp=""
result=""
for i in range(0,len(str)):
    x=str[i].isnumeric()
    if(x!=True):
        temp=temp+str[i]
    else:
        result=result+(temp*int(str[i]))
        temp=""
        
print(result)        

##str="ab2cd4efg5"
##temp=""
##result=""
##
##for i in range(0,len(str)):
##    x=str[i].isnumeric()
##    if(x!=True):
##        temp=temp+str[i]
##    elif(x==True):
##        for i in range(1,int(str[i])+1):
##            if(i%2!=0):
##                result=result+temp
##            elif(i%2==0):
##                temp1=temp[::-1]
##                result=result+temp1
##        temp=""
##print(result)


