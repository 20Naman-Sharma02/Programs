n=int(input("Enter a number:"))
i=0
while i<n:
    st=0
    while st<n-i:
        print("*",end="")
        st+=1
        u=0
    while u<=i:
        print("_",end="")
        u+=1
        st2=i-1
    while st2>=0:
        print("_",end="")
        st2-=1
    i+=1
    print()
    
    
