roman=input("Enter the Integer number to find the equivalent Roman Numerals: ")
num=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
sym=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]

rom_dic={1000:"M",900:"CM",500:"D",400:"XD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}
number=0

for i in range(0,len(roman)):
    print("rom",roman[i:i+2])
    if roman[i:i+2] in sym:
        x=sym.index(roman[i:i+2])
        number=number+num[x]
    else:
        if roman[i] in sym:
            y=sym.index(roman[i])
            number=number+num[y]
print(number)
