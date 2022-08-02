def inputThenPrintSumAndAverage():
    x=0
    count=0
    while True:
        num=input("Enter the Number: ")
        if(num.isnumeric()):
            x=x+int(num)
            count=count+1
        else:
            print("SUM =",x,end="  ")
            print("AUG =",int(x/count))
            break
            

inputThenPrintSumAndAverage()
