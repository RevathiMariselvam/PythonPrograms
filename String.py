##a="Hi"
##print(a*2)
##
##print()
##
##b=input("Enter the string: ")
##d=int(input("Enter the no. of times to be repeated: "))
##c=b[0:3]*d
##print(c)
##
##print()
##
##a=input("Enter the word to check the Palindrome: ")
##b=a[::-1]
##if(a==b):
##    print(f"Given {a} is Palindrome")
##else:
##    print(f"Given {a} is not Palindrome")
##
##print()
##
##a=input("Enter the word to check whether it is Symmetrical or Palindrome: ")
##b=len(a)%2
##if(b==0 or b!=0):
##    c=a[::-1]
##    d=len(a)//2
##    e=a[:d:]
##    f=a[d::]
##    if(a==c and e==f):
##        print(f"Given word \"{a}\" is both Palindrome and Symmetrical")
##    elif(a==c):
##        print(f"Given word \"{a}\" is Palindrome")
##    elif(e==f):
##        print(f"Given word is \"{a}\" Symmetrical")
##    else:
##        print(f"Given string \"{a}\" is not Symmetrical and Palindrome")
##print()
##
##
##a=str(input("Enter the word: "))
##b=len(a)
##if(b<3):
##    print("Enter the word more than three letters")
##else:
##    b=a[-3::]
##    if(b=="ing"):
##        c=a+"ly"
##        print(c)
##    else:
##        c=a+"ing"
##        print(c)
##
##print()
##
##sen=input("Enter the sentence to find the No. of vowels: ")
##a=sen.count("a")
##e=sen.count("e")
##i=sen.count("i")
##o=sen.count("o")
##u=sen.count("u")
##print("No. of vowels in the given sentence:",a+e+i+o+u)
##
##print()
##
##word=input("Enter the sentence to replace the string with the space: ")
##x=input("Enter the letter to replace the space: ")
##new_word=word.replace(" ",x)
##print(f"Now the space is replaced with the {x}: {new_word}")
##
##print()
##
##name=input("Enter the string:")
##name_list=[]
##for i in range(0,len(name)):
##    name_list.append(name[i:i+1])
##print(name_list)
##fin=input("Enter the element to find the positive and negative indexes: ")
##x=name_list.index(fin)
##print("Positive Index value is:",x)
##for i in range(-len(name_list),0):
##     if fin in name_list[i]:
##         print("Negative Index value is:",i)
##
##print()
##
##str1=input("Enter the string1: ")
##str2=input("Enter the string2: ")
##str1_lst=[]
##str2_lst=[]
##
##comman=[]
##unique=[]
##for i in range(0,len(str1)):
##    str1_lst.append(str1[i:i+1])
##
##for i in range(0,len(str2)):
##    str2_lst.append(str2[i:i+1])
##
##for i in range(0,len(str1_lst)):
##    for j in range(0,len(str2_lst)):
##        if(str1_lst[i]==str2_lst[j]):
##            if str1_lst[i] not in comman:
##                comman.append(str1_lst[i])
##
##unique=str1_lst+str2_lst
##for i in range(0,len(unique)):
##    if unique[i] not in comman:
##        temp.append(unique[i])
##
##print("Common Letters are:",comman)
##print("Unique Letters are:",temp)
##
##            

def str(x):
    length=int(len(x)/2)
    if (len(x))%2!=0 and x[length]=="Y" and (len(x[0:length])+1)==len(x[length:]):
        return True
    elif (len(x))%2==0 and x[length]=="Z" and (len(x[0:length]))==len(x[length:]):
        return True
    else:
        return False


x="AAAAXYZBBB"
cond=str(x)
print(f"The string {x} returns:", cond)








