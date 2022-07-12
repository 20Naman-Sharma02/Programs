n=int(input("Enter anumber"))
i=1
while i<=n:
    sp=0
    while sp<=n-i:
        print(" ",end="")
        sp+=1
    st=0
    while st<i:
        print("*",end="")
        st+=1
    st2=i-1
    while st2>=1:
        print("*",end="")
        st2+=1
    i+=1
    print()
        
