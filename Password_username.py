def existing():
    print("\n")
    ex_user=input("Enter the User Name to Login: ")
    ex_password=input("Enter the Password: ")
    if ex_user in user:
        for j in dic:
            if j==ex_user and dic[j]==ex_password:
                print("You are now Login")
                return True
            elif j==ex_user and dic[j]!=ex_password:
                for i in range(4):
                    if(i<=2):
                        ex_password=input("Enter the Correct Password: ")
                        for j in dic:
                            if j==ex_user and dic[j]==ex_password:
                                print("You are now Login")
                                return True
                    elif(i==3):
                        print("Limit Exceeds, Change Password or Re-Login Again")
                        x=int(input("Enter \"3\" If you want to change the Password: "))
                        if(x==3):
                            forgot()
    elif ex_user not in user:
        print("\n")
        print("User Name doesn't Exits, Create New Account")
        u=int(input("Enter \"2\" to Create New Account or \"3\" to Re-Login again: "))
        if(u==2):
            new()
        elif(u==3):
            existing()
                    


def forgot():
    print("\n")
    user_forg=input("Enter the User Name to Change Password: ")
    pass_forg=input("Enter the New Password: ")
    if user_forg not in user:
        print("Enter the Correct User Name")
    else:
        for i in dic:
            if i==user_forg:
                dic[i]=pass_forg
                print("Now the Password has been changed")
                print("Now Again Login with New Password")
                existing()

def new():
    print("\n")
    new_user=input("Enter the New User: ")
    new_pass=input("Enter the Password: ")
    dic.update({new_user:new_pass})
    user.append(new_user)
    password.append(new_pass)
    existing()


dic={"revathi2501":"Revathi@25","krishanth2411":"Krish@24","ashok0408":"Ashok@408"}

x=dic.keys()
user=[]
y=dic.values()
password=[]
for i in x:
    user.append(i)
for i in y:
    password.append(i)


print("1. Existing User: Login ")
print("2. New User")
print("3. Forget password")
login=int(input("Enter operations to be done: "))

if(login==1):
    existing()
elif(login==2):
    new()
elif(login==3):
    forgot()
elif(login==4):
    breaking()
else:
    print("Enter the correct number")
    

