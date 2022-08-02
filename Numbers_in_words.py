def last(num):
    global x
    for i in spell:
        if(i==num[-1]):
            x=x+spell[i]
    print(x)

def tens(num):
    global x
    for i in spell:
            if(i==num[-2]):
                if(num[-2]=="1"):
                    for j in teen:
                        if(j==num[-2]+num[-1]):
                            x=x+teen[j]
                            print(x)
                elif(num[-1]=="0"):
                    for j in ten:
                        if(j==num[-2]+num[-1]):
                            x=x+ten[j]
                            print(x)
                elif(num[-2]=="0"):
                    last(num)
                elif(num[-2]!="1" and num[-2]!="0"):
                    for i in ten:
                        if(i==num[-2]+"0"):
                            x=x+ten[i]
                    last(num[-1])

def hundred(num):
    global x
    for i in spell:
        if(i==num[-3] and num[-2]+num[-1]=="00"):
            x=x+spell[i]+" Hundred "
            print(x)
        elif(i==num[-3] and num[-2]=="1"):
            for j in teen:
                if(j==num[-2]+num[-1]):
                    x=x+spell[i]+" Hundred and "+teen[j]
                    print(x)
        elif(i==num[-3] and num[-2]=="0"):
            x=x+spell[i]+" Hundred and "
            last(num[-1])
        elif(i==num[-3] and num[-3]=="0"):
            tens(num)
        elif(i==num[-3] and num[-1]=="0"):
            x=x+spell[i]+" Hundred "
            tens(num)
        elif(i==num[-3] and num[-2]!="0" and num[-1]!="0"):
            x=x+spell[i]+" Hundred "
            tens(num)



def thousand(num):
    global x
    for i in spell:
        if(i==num[-4] and num[-3]+num[-2]+num[-1]=="000"):
            x=x+spell[i]+" Thousand "
            print(x)
        elif(i==num[-4] and num[-4]=="0"):
            hundred(num)
        elif(i==num[-4] and num[-3]+num[-2]=="00" and num[-1]!="0"):
            x=x+spell[i]+" Thousand and "
            last(num)
        elif(i==num[-4]):
            x=x+spell[i]+" Thousand "
            hundred(num)
##        elif(i==num[-4] and num[-4]!="0" and num[-3]!="0" and num[-2]!="0" and num[-1]=="0"):
##            x=x+spell[i]+" Thousand "
##            hundred(num)
##        elif(i==num[-2])

##def teen_thousand(num):
##    global x
##    for i
num=input("Enter the Four Digit Number to spell out:")
spell={"0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
teen={"10":"Ten","11":"Eleven","12":"Twelve","13":"Thirteen","14":"Fourteen","15":"Fifteen","16":"Sixteen","17":"Seventeen","18":"Eighteen","19":"Nineteen"}
ten={"10":"Ten ","20":"Twenty ","30":"Thirty ","40":"Fourty ","50":"Fifty ","60":"Sixty ","70":"Seventy ","80":"Eighty ","90":"Ninety "}
x=""

##elif(len(num)==5):
##    teen_thousand(num)



