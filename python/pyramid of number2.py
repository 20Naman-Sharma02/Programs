n=int(input("Enter a number:"))
i=1
while i<=n:
    s1=0
    while s1<n-i:
        print(" ",end="")
        s1+=1
    j=0
    while j<i:
        print(i-j,end="")
        j+=1
    j=2
    while j<=i:
        print(j,end="")
        j+=1
    i+=1
    print()
