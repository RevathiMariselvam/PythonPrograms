month=int(input("Enter the Month number: "))
year=int(input("Enter the Year: "))

if(month<=12):
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        print("31 Days in this month")
    elif(month==2):
        if(year%4==0 and (year%400==0 or year%100!=0)):
            print("29 Days in this month")
        else:
            print("28 Days in this month")
    else:
        print("30 Days in this month")
else:
    print("Enter the Correct Month")
