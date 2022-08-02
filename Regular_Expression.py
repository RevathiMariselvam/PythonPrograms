import re

##pattern=r"^[6-9]\d{9}$"
##
##string="9944757342"
##
##a=re.findall(pattern,string)
##b=re.search(pattern,string)
###print(a)
##if b:
##    print("Given phone number is valid")
##else:
##    print("Invalid Phone number")

patt="[A-Z]{5}[0-9]{4}[A-Z]"
str="AAAAA1234A"

c=re.search(patt,str)

if c:
    print(f"Given Pan Card Number {str} is valid")
else:
    print(f"Given Pan Card Number{str} is Invalid")

pattern=r"^\b[a-z0-9]+[@]+\b[a-z]+[.]+[a-z]{2,3}$"
string="revathimselvam@gmailcom"

d=re.search(pattern,string)

if d:
    print(f"Given E-Mail ID {string} is valid")
else:
    print(f"Given E-Mail ID {string} is invalid")
