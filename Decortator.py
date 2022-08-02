####return the function

##def add():
##    print("Addition of 2 Number:")
##    def inner(a,b):
##        print(a+b)
##    return inner
##
##a=add()
##a(2,3)


####
##
##def add(result):
##    print("Square the value:")
##    result(10)
##
##def result(a):
##    print(a**2)
##
##add(result)
##
##def outer(func):
##    print("outer function")
##    def inner():
##        print("ocean academy")
##        func()
##        print("thank you")
##    print("inner function is calling")
##    return inner
##
####
####@outer
####def hello():
####    print("hello good morning")
##    
##@outer
##def hello1():
##    print("hello2")
##
####outer(hello)
##print("out")
##hello1()


##def chain(func):
##    print("chain")
##    def chaininner(a,b):
##        
##        print("chain decorators starts")
##        func(a,b)
##        print("chain decorators ends")
##    return chaininner
##
##def outer(func):
##    print("outer")
##    def inner(a,b):
##        if(b!=0):
##            func(a,b)
##        else:
##            print(0)
##    return inner
##
##
##@chain
##@outer
##def div(a,b):
##    print(a/b)
##
##div(2,0)
##div(2,1)
####################

def chain(func):
    def chaininner():
        print("******************")
        func()
        print("******************")
    return chaininner

def outer(func):
    def inner():
        print("Hi")
        func()
    return inner
        

@chain
@outer
def hello():
    print("Hello")

hello()






