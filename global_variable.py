def add():
    global x
    x=int(input("Enter the value of x: "))
    y=20
    print("sum of 2 numbers inside function:",x+y)

x=10
y=10
print("sum of 2 numbers before calling function:",x+y)
add()
print("sum of 2 numbers outside function:",x+y)
