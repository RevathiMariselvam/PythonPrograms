import pymongo

connect=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=connect["Login_Database"]
mycol=mydb["UserName and Password List"]

##data=[{"Username":"revathi2501","Password":"Revathi@25"},
##      {"Username":"krishanth2411","Password":"Krish@24"},
##      {"Username":"ashok0408","Password":"Ashok@408"},
##      {"Username":"viji1507","Password":"Viji@1507"}]
##mycol.insert_many(data)

def existing():
    print("\n")
    ex_user=input("Enter the User Name to Login: ")
    ex_password=input("Enter the Password: ")
    for data in mycol.find():
        if(data["Username"]==ex_user and data["Password"]==ex_password):
            print("Your are now Login")
            return True
        elif(data["Username"]==ex_user and data["Password"]!=ex_password):
             for i in range(4):
                if(i<=2):
                    ex_password=input("Enter the Correct Password: ")
                    for j in mycol.find():
                        if j["Username"]==ex_user and j["Password"]==ex_password:
                            print("You are now Login")
                            return True
                elif(i==3):
                    print("Limit Exceeds, Change Password or Re-Login Again")
                    x=int(input("Enter \"3\" If you want to change the Password: "))
                    if(x==3):
                        forgot()
    else:
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
    for data in mycol.find():
        if (user_forg==data["Username"]):
            myquery={"Password":data["Password"]}
            newvalues={"$set":{"Password":pass_forg}}
            mycol.update_one(myquery, newvalues)
            print("Now the Password has been Changed")
            print("Now Again Login with New Password")
            existing()
            return True
    else:
        print("Enter the Correct Username")
        forgot()

def new():
    print("\n")
    new_user=input("Enter the New User: ")
    new_pass=input("Enter the Password: ")
    newvalues={"Username":new_user,"Password":new_pass}
    mycol.insert_one(newvalues)
    existing()


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
    

