try:
    st=input("Enter the String: ")
    vo=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    x=st.isnumeric()
    if x==True:
        raise Exception
    else:
        for i in range(0,len(st)):
            if st[i] in vo:
                count+=1
        print("No. of Vowels:", count)
except:
    print("You have typed the numeric value")
