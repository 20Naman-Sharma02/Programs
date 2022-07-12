n=int(input("Enter a number"))
i=0
while i<n:
    sp=0
    while sp<=i:
        print(" ",end="")
        sp+=1
    st=0
    while st<n-i:
        print("*",end=" ")
        st+=1
        print()
        sp1=0
        while sp1<n-i:
            print(" ",end="")
            sp1+=1
            st1=0
        while st1<i:
            print("*",end=" ")
            st1+=1
    i+=1
    print()
