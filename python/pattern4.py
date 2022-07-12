n=int(input("Enter a number:"))
i=0
p=i
while i<=n:
    j=0
    while j<=i:
        print(p+1,end=" ")
        p+=1
        j+=1
    i+=1
    print()
