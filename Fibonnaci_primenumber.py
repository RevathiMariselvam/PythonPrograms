def prime(a):
       global count
       if((a>=3 and a%2!=0) or a==2):
           for i in range(a-1,2,-1):
                if(a%i==0 or a==i):
                   break
           else:
                print(a,end=" ")
                count+=1

limit=int(input("Enter the Fibonnaci prime numbers to diplay: "))
a=0
b=1
c=0
count=0
#print(2,end=" ")
while(count!=limit):
       c=a+b
       prime(a)
       a=b
       b=c
   
