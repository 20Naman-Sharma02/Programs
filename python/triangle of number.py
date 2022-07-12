n=int(input("Enter a anumber:"))
i=1
while i<=n:
    s=0
    while s<n-i:
        print(" ",end="")
        s+=1
    num=0
    while num<i:
        print(n-i+1,end="")
        num+=1
    i+=1
    print()
    
        
