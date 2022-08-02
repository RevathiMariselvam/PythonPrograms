name_1=input("Enter the Person_1 Name: ")
age_1=int(input("Enter the Person_1 Age: "))
name_2=input("Enter the Person_2 Name: ")
age_2=int(input("Enter the Person_2 Age: "))
name_3=input("Enter the Person_3 Name: ")
age_3=int(input("Enter the Person_3 Age: "))
name_4=input("Enter the Person_4 Name: ")
age_4=int(input("Enter the Person_4 Age: "))

if(age_1>age_2 and age_1>age_3 and age_1>age_4):
    print(f"{name_1} is Elderest of all")
elif(age_2>age_1 and age_2>age_3 and age_2>age_4):
    print(f"{name_2} is Elderest of all")
elif(age_3>age_1 and age_3>age_2 and age_3>age_4):
    print(f"{name_3} is Elderest of all")
elif(age_4>age_1 and age_4>age_2 and age_4>age_3):
    print(f"{name_4} is Elderest of all")

if(age_1<age_2 and age_1<age_3 and age_1<age_4):
    print(f"{name_1} is Youngest of all")
elif(age_2<age_1 and age_2<age_3 and age_2<age_4):
    print(f"{name_2} is Youngest of all")
elif(age_3<age_1 and age_3<age_2 and age_3<age_4):
    print(f"{name_3} is Youngest of all")
elif(age_4<age_1 and age_4<age_2 and age_4<age_3):
    print(f"{name_4} is Youngest of all")
