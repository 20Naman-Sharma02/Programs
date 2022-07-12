n=int(input("enter a number:"))
i=1
while i<=n:
    j=1
    while j<=n:
        if j==i:
            print("*",end="")
        else:
            print(0,end="")
        j+=1
    print("*",end="")
        
    j1=1
    while j1<=n:
        if i+j1==n+1:
            print("*",end="")
        else:
            print(0,end="")
        j1+=1
    i+=1
    print()
    
