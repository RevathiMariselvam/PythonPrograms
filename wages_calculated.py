age=int(input("Enter the age: "))
sex=str(input("Enter the Sex(M/F): "))
work=int(input("Enter the No. of days worked: "))
if(sex=="M" or sex=="F"):
    if(sex=="M"):
        if(age>=18 and age<30):
            salary=work*700
            print(f"Your Salary is: {salary}")
        else:
            salary=work*600
            print(f"Your Salary is: {salary}")
    elif(sex=="F"):
        if(age>=18 and age<30):
            salary=work*750
            print(f"Your Salary is: {salary}")
        else:
            salary=work*650
            print(f"Your Salary is: {salary}")    
else:
    print("Enter the Correct sex(M/F)")
