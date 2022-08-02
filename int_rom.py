##int_num=int(input("Enter the Integer number to find the equivalent Roman Numerals: "))
##dic={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"XD",500:"D",900:"CM",1000:"M"}
##
##for i in dic:
##    quotient=int_num//i
##    int_num=int_num%i
##    print(quotient,int_num)
##    
    
    
##def printRoman(number):
##    num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
##    sym=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
##    i=12
##      
##    while number:
##        div=number//num[i]
##        number%=num[i]
##        while div:
##            print(sym[i],end="")
##            div-=1
##        i-=1
##  
###Driver code
###if __name__ == "__main__":
number=int(input("Enter the Integer number to find the equivalent Roman Numerals: "))
num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
sym=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
i=12
roman=""

while number:
    div=number//num[i]
    number%=num[i]
    while div:
        roman+=sym[i]
        div-=1
    i-=1

##dic={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"XD",500:"D",900:"CM",1000:"M"}
##num_str=str(number)
##add=""
##for i in range(len(num_str)-1,-1,-1):
##    temp=int(num_str[i]+add)
##    print(temp)
##    if int(temp) in num:
##        x=num.index(int(temp))
##        roman=rom[x]+roman
##    if temp not in num:
##        for i in range(0,len(num)):
##            for j in range(0,len(num)):
##                if((num[i]+num[j])==temp):
##                    y=num.index(num[i])
##                    roman=rom[y]+roman
##                elif(num[i]<temp):
##                    z=num.index(num[i])
##                    roman=rom[z]+roman
##    add=add+"0"

print("Integer to Roman:",roman)
    

