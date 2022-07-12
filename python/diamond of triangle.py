n=int(input("Entera number:"))
i=1
while i<=n:
    sp=0
    while sp<n-i:
        print(" ",end="")
        sp+=1
    st=0
    while st<i:
        print("*",end=" ")
        st+=1
    i+=1
    print()
    
