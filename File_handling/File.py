###f=open("Mytext.txt","x")
##f1=open("Mytext.txt","w")
##f1.write("""Hello
##welcome
##India\n""")
##f1.close()
##
##f3=open("Mytext.txt","a")
##f3.write("Ocean Academy")
##f3.close()
##f2=open("Mytext.txt","r")
####print(f2.readline())
####print(f2.readline())
####print(f2.readline())
##print(f2.readlines())
####for i in f2:
####    print(i)
##
##f2.close()
##
##

try:
    f1=open("text.txt","r")
except FileNotFoundError:
    print("File is not Exist")
else:
    f1=open("text.txt","a")
    f1.write("Hello")
    f1.close()
