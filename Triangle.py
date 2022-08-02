a=int(input("Enter the 1st side of the triangle: "))
b=int(input("Enter the 2nd side of the triangle: "))
c=int(input("Enter the 3rd side of the traingle: "))
if(a==b and b==c and a==c):
    print("Triangle is Equivalateral traingle")
elif(a==b or b==c or a==c):
    print("Traingle is Isoceles triangle")
else:
    print("Traingle is scalene traingle")  
    
