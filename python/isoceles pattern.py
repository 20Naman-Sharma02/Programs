n=int(input("Enter anumber:"))
i=1
while i<=n:
    s=0
    while s<=n-i:
        print(" ",end="")
        s+=1
    st=0
    p=0
    while st<i:
        print("*",end="")
        st+=1
    p=i-1
    while p>=1:
        print("*",end="")
        p-=1
        
    i+=1
    print()
    
    
