class CommonDivisor:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def getGreatestCommonDivisor(self):
        x_div=[]
        y_div=[]
        temp=[]
        if(x<10 or y<10):
            return(-1)
        else:
            for i in range(2,11):
                if(x%i==0):
                    x_div.append(i)
                if(y%i==0):
                    y_div.append(i)
            if(set(x_div) & set(y_div)):
                temp=list(set(x_div) & set(y_div))
                return(max(temp))
        
                
                
            

x=int(input("Enter the value of one parameter:"))
y=int(input("Enter the value of another parameter:"))


obj=CommonDivisor(x,y)
z=obj.getGreatestCommonDivisor()
print("Common Divisor:",z)
