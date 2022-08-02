##a=[1,2,3,4,5]
##b=[6,7]
####print(a[-1:-3:-1])
####a.append(b)
####print(a)
####c.extend(b)
###print(a)
##c=a+b
##print(c)
##
##a=[]
##b=[]
##e=[]
##c=0
##d=len(a)
##for i in range(0,5):
##    b=int(input("Enter the list values: "))
##    a.append(b)
##    c+=a[i]
##    e.append(a[i]**2)
##print("Sum of the numbers in the list:",c)
##print("Square the list value:",e)
##
##print()
##
##
##alph=["A","B","C","D","E"]
##for i in range(0,len(alph)):
##    for j in range(0,len(alph)):
##        print(alph[i],end=" ")
##    print()
##
##print()
##
##for i in range(0,len(alph)):
##    for j in range(0,len(alph)):
##        print(alph[j],end=" ")
##    print()
##
##print()
##
##alph=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
##k=0
##for i in range(0,5):
##    for j in range(0,5):
##        print(alph[k],end=" ")
##        k+=1
##    print()
##
##print()
##
##alph=[1,2,3,4]
##cop=[]
##length=len(alph)
##i=0
##while(length!=0):
##    store=alph[length-1]
##    cop.append(store)
##    length-=1
##    i+=1
##print("Reversed List",cop)
##
##a=65
##for i in range(0,5):
##    for j in range(0,5):
##        print(chr(a),end=" ")
##        a+=1
##    print()
##
##print()
##
##for i in range(0,5):
##    a=65
##    for j in range(0,5):
##        print(chr(a),end=" ")
##        a+=1
##    print()
##
##print()
##
##a=65
##for i in range(0,5):
##    for j in range(0,5):
##        print(chr(a),end=" ")
##    a+=1
##    print()
##
##print()
##
##num=[2,3,4,5,1,4,6,5,2,1]
##temp_list=[]
##temp=num
##num1=len(temp)
##for i in range(0,num1):
##    if num[i] not in temp_list:
##        temp_list.append(num[i])
##print(f"From the list {num} Removed the duplicate elements now:",temp_list)
##
##
##
##b=[5,6,8,1,3,4,2,7]
##num=[]
##for i in range(0,len(b)):
##    for j in range(i+1,len(b)):
##        if(b[i]>=b[j]):
##            b[i],b[j]=b[j],b[i]
##print(b)
##
##print()
##
##b=[5,6,8,1,3,4,2,7]
##num=[]
##for i in range(0,len(b)):
##    for j in range(i+1,len(b)):
##        if(b[i]<=b[j]):
##            b[i],b[j]=b[j],b[i]
##print(b)
##
##print()
##
##lst=[]
##count=0
##a=int(input("Enter the length of the list:"))
##for i in range(0,a):
##    b=input("Enter the list value: ")
##    lst.append(b)
##print("Given list is:",lst)
##
##for i in range(0,a):
##    temp=lst[i]
##    if(temp[0:1]==temp[-1::]):
##        count+=1
##print(f"{count} elements have same first and last letters")
##
##print()
##
##lst=[]
##if(len(lst)==0):
##    print("List is empty")
##else:
##    print("List has some value")
##print()
##
count=0
lst4=[2,3,4,5,7,7,7,11,7,2,2]
new=[]
b=len(lst4)
for i in range(0,b):
    if(i<b):
        num=lst4[i]
        a=lst4.count(num)
        b=len(lst4)
        if(a>1):
            for j in range(0,a-1):
                if num not in new:
                    new.append(num)
                lst4.remove(num)
                b=len(lst4)
            print(f"The element {num} is repeated {a} times")

#print(f"The element {new} is the common element for both the list")
##
##print()
##        
##lst1=[1,2,3,4,5,6,8]
##lst2=[5,6,7,8,9]
##lst3=[]
##
##for i in range(0,len(lst1)):
##    for j in range(0,len(lst2)):
##        if(lst1[i]==lst2[j]):
##            lst3.append(lst1[i])
##print("Common element in both the list:",lst3)
##
##print()
##
##time=input("Enter the time: (HH:MM): ")
##clock=time.split(":")
##hr_clo=int(clock[0])
##min_clo=int(clock[1])
##day=input("Enter the day: (su,mo,tu,we,th,fr,sa): ")
##duration=input("Enter the call duration: ")
##hrmin=duration.split(":")
##hr=int(hrmin[0])
##minu=int(hrmin[1])
##tot_min=(hr*60)+minu
##if(hr_clo>=1 and hr>=1):
##    if(day=="su" or day=="sa"):
##        cost=(tot_min*0.15)
##        print(f"Total cost is {cost}")
##    elif(day=="mo" or day=="tu" or day=="we" or day=="th" or day=="fr" or day=="sa"):
##        if(hr_clo>=8 and hr_clo<=18):
##            cost=(tot_min*0.25)
##            print(f"Total cost is {cost}")
##        elif(hr_clo>=19 and hr_clo<=24 or hr_clo>=1 and hr_clo<=7):
##            cost=(tot_min*0.45)
##            print(f"Total cost is {cost}")
##        else:
##            print("incorrect Days")
##    else:
##        print("incorrect Days")
##else:
##    print("incorrect Time")
##            
##
##
##print()
##
##count=0
##num_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
##l1=[]
##l2=[]
##print("Whole List",num_list)
##for i in range(0,len(num_list),2):
##    l1.append(num_list[i])
##print("List1:",l1)
##
##for i in range(0,len(l1)):
##    count=count+l1[i]
##avg_l1=count/len(l1)
##print("Average of the numbers in the list is: ",avg_l1)
##
##for i in range(0,len(num_list),3):
##    l2.append(num_list[i])
##print("List2:",l2)
##
##count=0
##for i in range(0,len(l2)):
##    count=count+l2[i]
##avg_l2=count/len(l2)
##print("Average of the numbers in the list is: ",avg_l2)
##
##
##
##print()
##
##num=""
##input_list=[10,20,30,40,50]
##for i in range(0,len(input_list)):
##    num=num+str(input_list[i])
##print(f"Numbers in the list \"{input_list}\" is Concatenated: ",num)
##
##print()
##
##lst=[0,1,2,3,4,5]
##print("Input List:",lst)
##for i in range(0,len(lst),2):
##    lst[i],lst[i+1]=lst[i+1],lst[i]
##print("Position of the element is changed now:",lst)
##
##str=input("Enter the string: ")
##lst=[]
##temp=[]
##for i in range(0,len(str)):
##    lst.append(str[i])
##    #print(lst)
##
##for i in range(0,len(lst)):
##    x=lst.count(lst[i])
##    if lst[i] not in temp:
##        print(f"{lst[i]} is {x} times")
##        temp.append(lst[i])
##        #print(temp)
##    
##
##print()
##    
##lst1=[10,20,30,40,50]
##print(f"Difference between the largest and smallest value in the list {lst1} is {max(lst1)-min(lst1)}")
##
##print()
##
##length=int(input("Enter the length of the list: "))
##lst=[]
##print("Enter the list value: ")
##for i in range(0,length):
##    lst_value=int(input())
##    lst.append(lst_value)
##
##lst_even=[]
##lst_odd=[]
##for i in range(0,length):
##    if(lst[i]%2==0):
##        lst_even.append(lst[i])
##    else:
##        lst_odd.append(lst[i])
##print("Total element in the list is",len(lst))
##print(f"There are {len(lst_odd)} Odd numbers in the list, and the odd list is {lst_odd}")
##print(f"There are {len(lst_even)} Even numbers in the list, and the even list is {lst_even}")
##
##print()
##
##lst=[-5,-4,4,-5,2,-3,5,8,-9]
##temp=[]
##for i in range(0,len(lst)):
##    if(lst[i]>0):
##        temp.append(lst[i])
##print("Input list is:",lst)
##print("Deleted the negative value:",temp)
##
##print()
##
##lst=[1,2,9,19,29,30,45,49]
##temp=[]
##for i in range(0,len(lst)):
##    x=str(lst[i])
##    if(x[len(x)-1:len(x)]=="9"):
##        continue
##    else:
##        temp.append(int(x))
##print("Input List is:",lst)
##print("Omitted the value ends with \"9\":",temp)        
##
##print()
##
##lst=[1,2,9,19,29,30,45,49]
##temp=[]
##for i in range(0,len(lst)):
##    if(lst[i]%10==9):
##        continue
##    else:
##        temp.append(lst[i])
##print("Input List is:",lst)
##print("Omitted the value ends with \"9\":",temp)        
##
##
##print()
##
##lst=[1,2,3,4,15,6]
##print("List is",lst)
##for i in range(0,len(lst)):
##    for j in range(0,len(lst)):
##        if(lst[i]>lst[j]):
##            lst[i],lst[j]=lst[j],lst[i]
##print("Second highest value is:",lst[1])
##            
##print()
##
##
##lst1_len=int(input("Enter the length of list 1: "))
##lst2_len=int(input("Enter the length of list 2: "))
##lst1=[]
##lst2=[]
##temp=[]
##print("Enter the list 1 value:")
##for i in range(0,lst1_len):
##    lst1.append(input())
##print("List1:", lst1)
##
##print("Enter the list 2 value:")
##for j in range(0,lst2_len):
##    lst2.append(input())
##print("List2",lst2)
##
##for i in range(0,lst1_len):
##    for j in range(0,lst2_len):
##        if(lst1[i]==lst2[j]):
##            temp.append(lst1[i])
##print("Common element in both the list are:",temp)
##print()
##
##lst=[1,2,3,4]
##word=input("Enter the string you need to insert before the element in the list: ")
##for i in range(0,len(lst)):
##    lst[i]=word+str(lst[i])
##print(f"The word {word} is added to the element in the list, then the output:",lst)
##
##print()

##lst=[3,4,0,0,0,6,2,0,6,7,0,0,0,9,10,7,4,4,5,3,0,0,2,9,7,1]
##print("Input List:\n",lst)
##count=len(lst)-1
##for i in range(0,len(lst)):
##    if lst[i]==0:
##        lst.remove(0)
##        lst.insert(count,0)
##        count+=1
##print(f"All Zeroes are moved to end elements, Now the output list:\n {lst}")
##        

##print()
##
##count=0
##temp=[]
##lst=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
##for i in range(0,len(lst)):
##    count=0
##    for j in range(0,len(lst[i])):
##        count=count+lst[i][j]
##    temp.append(count)
##
##temp_list=[]
##for i in range(0,len(temp)):
##    temp_list.append(temp[i])
##
##for i in range(0,len(temp_list)):
##    for j in range(0,len(temp_list)):
##        if(temp_list[i]>temp_list[j]):
##            temp_list[i],temp_list[j]=temp_list[j],temp_list[i]
##x=temp.index(temp_list[0])
##
##print(f"The element list {lst[x]} has the highest sum value of {temp_list[0]}")
##

##print()
##
##str="the quick brown fox jumps over the lazy dog"
##lst=str.split(" ")
##print("List with \"the\":",lst)
##
##for i in lst:
##    if "the" in lst:
##        lst.remove("the")
##print("List without \"the\":",lst)
##
##count=[]
##for i in lst:
##    x=len(i)
##    count.append(x)
##print("Length of the Word:",count)
##

print()
##
##lst=["Arun","Preethi","antony","kavitha","ashok","Elango","Ishwarya","Revathi","selvam"]
##print(lst)
##temp=[]
##vowels=["A","E","I","O","U","a","e","i","o","u"]
##for i in lst:
##    if i[0] in vowels:
##        temp.append(i)
##print("Deleted the name start without vowels:",temp)
##        

