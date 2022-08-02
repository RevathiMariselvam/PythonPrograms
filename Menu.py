def add():
    temp_list=[]
    print("\n")
    print("1. Add One Element")
    print("2. Add a List")
    print("3. Go to Main Menu")
    value_add=int(input("Enter the Operations to be done: "))
    if(value_add==1):
        len_add=int(input("Enter the number of elements to be added in the list: "))
        print("Enter the element to add: ")
        for i in range(0,len_add):
            num_add=input()
            temp_list.append(num_add)
        list_value.extend(temp_list)
        print("New element is added in the list:",list_value)
    elif(value_add==2):
        len_add=int(input("Enter the length of the list to be added: "))
        print("Enter the new list value to be added:")
        for i in range(0,len_add):
            num_add=input()
            temp_list.append(num_add)
        print("This was the new list going to be added in the Main list:",temp_list)
        list_value.append(temp_list)
        print("Both list are added: ",list_value)
    elif(value_add==3):
        main_menu()
    else:
        print("Enter the correct Number")

def modify():
    print("\n")
    print("1. Replace the particular position element")
    print("2. Swap the element position")
    print("3. Go to Main Menu")
    value_modify=int(input("Enter the Operations to be done: "))
    if(value_modify==1):
        len_mod=len(list_value)
        mod_value=int(input("Enter the position of the element to be replace: "))
        if(mod_value<len_mod):
            list_value.remove(list_value[mod_value])
            repl=input("Enter the element value to be replaced: ")
            list_value.insert(mod_value,repl)
            print(f"Now the element are replaced in the {mod_value}: {list_value}")
        else:
            print("Given position exceeds the length of the list")
    elif(value_modify==2):
        ele1=int(input("Enter the 1st position of the list to be swapped: "))
        ele2=int(input("Enter the 2st position of the list to be swapped: "))
        list_value[ele1],list_value[ele2]=list_value[ele2],list_value[ele1]
        print("Two position elements are swapped now:",list_value)
    elif(value_modify==3):
        main_menu()
    else:
         print("Enter the correct Number")

def delete():
    print("\n")
    print("1. Delete the element by position")
    print("2. Delete the element by value")
    print("3. Go to Main Menu")
    value_delete=int(input("Enter the Operations to be done: "))
    if(value_delete==1):
        count=len(list_value)
        pos_value=int(input("Enter the position of the element to be deleted: "))
        if(pos_value<=count-1):
            list_value.pop(pos_value)
            print(f"Now the element in the {pos_value} is deleted: {list_value}")
        else:
            print("Given position exceeds the length of the list")
    elif(value_delete==2):
        ele_value=input("Enter the element value to be delete: ")
        count=list_value.count(ele_value)
        if(count>=1):
            list_value.remove(ele_value)
            print("Now the given element is deleted in the list",list_value)
        else:
            print("Given element is not in the list")
    elif(value_delete==3):
        main_menu()
    else:
         print("Enter the correct Number")
         
def sort():
    print("\n")
    print("1. Ascending Order")
    print("2. Descending Order")
    print("3. Go to Main Menu")
    value_sort=int(input("Enter the Operations to be done: "))
    if(value_sort==1):
        list_value.sort()
        print("List are now arranged in Ascending Order:",list_value)
    elif(value_sort==2):
        list_value.sort(reverse=True)
        print("List are now arranged in Descending Order:",list_value)
    elif(value_sort==3):
        main_menu()
    else:
        print("Enter the correct Number")
        
def  display():
    print("\n")
    print("1. Display the element by position")
    print("2. Display the position by element")
    print("3. Display the list")
    print("4. Go to Main Menu")
    value_display=int(input("Enter the Operations to be done: "))
    if(value_display==1):
        dis_ele=int(input("Enter the position of the element: "))
        print(f"In position {dis_ele} the element {list_value[dis_ele]} is in the list")
    elif(value_display==2):
        dis_ele=input("Enter the element to find its position: ")
        pos=list_value.index(dis_ele)
        print(f"The element {dis_ele} is in the position {pos}")
    elif(value_display==3):
        print("List: ",list_value)
    elif(value_display==4):                                                                                
        main_menu()
    else:
        print("Enter the correct Number")



def main_menu():
    print("\n")
    print("MENU")
    print("1.ADD")
    print("2.MODIFY")
    print("3.DELETE")
    print("4.SORT")
    print("5.DISPLAY")
    print("6.Exit")
    value=int(input("Manipulation Menu Number: "))
    while(value<=6):
        if(value==1):
            add()
        elif(value==2):
            modify()
        elif(value==3):
            delete()
        elif(value==4):
            sort()
        elif(value==5):
            display()
        elif(value==6):
            break
        else:
            print("You have typed the number which is not in the MENU list")
        

length=int(input("Enter the length of the list: "))
list_value=[]
print("Enter the list value:")
for i in range(0,length):
    num=input()
    list_value.append(num)
print("Main List: ",list_value)
main_menu()
