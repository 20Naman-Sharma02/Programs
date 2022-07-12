n=int(input("Enter a number:"))
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    s=0
    while s<n-i:
        print("*",end="")
        s+=1
    s1=0
    while s1<n-i:
        print("*",end="")
        s1+=1
    j=0
    while j<i:
        print(i-j,end="")
        j+=1
    i+=1
    print()
        
