n=int(input("Enter a number"))
i=1
p=1
while i<=6:
    j=0
    while j<=n-i:
        if j%2!=0:
            print("*",end="")
        else:
            print(p,end="")
            p+=1
        j+=1
    i+=1
    print()
    
