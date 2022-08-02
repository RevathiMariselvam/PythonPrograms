def four(roman):
    temp=""
    #nine={"VIV":"IX","XVX":,"LXL","CLC","DCD","MDM"}
    for i in range(0,len(roman)):
        x=roman.count(roman[i])
        if(x==4):
            temp=temp+roman[i]

    for j in range(len(num)):
        if(temp[0]==num[j]):
            temp1=temp[0]+num[j+1]

    roman=roman.replace(temp,temp1)
    
    print("Integer to Roman:",roman)

    

def printrom(roman):
    print("Integer to Roman:",roman)

int_num=int(input("Enter the Integer number to find the equivalent Roman Numerals: "))
##dic={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"XD",500:"D",900:"CM",1000:"M"}
rom_dic={1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
roman=""
remainder=10

num=["I","V","X","L","C","D","M"]


for j in rom_dic:
    if(int_num==j and int_num!=5):
        print(int_num,j)
        print("Integer to Roman:",rom_dic[j])
        break
    if(int_num>=j and remainder>=3):
        quotient=int_num//j
        remainder=int_num%j
        roman=roman+(quotient*rom_dic[j])
        if(remainder>=3):
            int_num=remainder
        else:
            roman=roman+(remainder*"I")
            if(remainder==4 or quotient==4):
                four(roman)
            else:
                printrom(roman)

                

