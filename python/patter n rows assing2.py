n=int(input("Enter a number:"))
i=1
print(1)
while i<n:
    j=0
    while j<=i:
        if j==0 or j==i:
            print(1,end="")
        else:
            print(2,end="")
        j+=1
    i+=1
    print()
