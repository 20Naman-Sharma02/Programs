n=int(input("Enter a number:"))
i=0
while i<n:
    j=0
    while j<=n-i:
        if j%2==0:
            print("*",end="")
        else:
            print(j,end="")
            j+=1
    i+=1
    print()
