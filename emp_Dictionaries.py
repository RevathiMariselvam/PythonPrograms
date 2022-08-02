emp=int(input("Enter the No. of Employees: "))
main={}
keys=[]
res={}


for i in range(0,emp):
    print("\n")
    name=input("Enter the Employee Name: ")
    age=int(input("Enter the Employee Age: "))
    salary=int(input("Enter the Employee Salary: "))
    des=input("Enter the Employee Designation: ")
    main.update({f"Employee{i+1}":{"Name":name,"Age":age,"Salary":salary,"Designation":des}})
print(main)

print("Enter the any Two key to display the details: ")
for i in range(0,2):
    keys.append(input())

for i in main.values():
    for j in i:
        if keys[0] in j:
            res.update({keys[0]:i[j]})
        if keys[1] in j:
            res.update({keys[1]:i[j]})
    print(res)
