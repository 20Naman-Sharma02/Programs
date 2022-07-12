n=int(input("Enter a number:"))
i=1
while i<=n:
    j=1
    while j<=n:
        if i%2==0:
            print("*",end=" ")
            j+=1
        else:
            print("%",end=" ")
            j+=1
    i+=1
    print()
    
