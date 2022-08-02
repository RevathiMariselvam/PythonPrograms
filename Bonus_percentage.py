name=input("Enter the Employee Name: ")
salary=int(input("Enter the Employee Salary: "))
exp_year=int(input("Enter the year of Experience: "))
if(exp_year>=1 and exp_year<60):
    if(exp_year>10):
        bonus=salary*0.1
        print(f"{name} will get the net bonus of {bonus}")
    elif(exp_year>=6 and exp_year<=10):
        bonus=salary*0.08
        print(f"{name} will get the net bonus of {bonus}")
    elif(exp_year<6):
        bonus=salary*0.05
        print(f"{name} will get the net bonus of {bonus}")
else:
    print("Enter the correct work experience")
