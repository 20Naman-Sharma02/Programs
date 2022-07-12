n=int(input("Enter a number:"))
i=0
while i<=n:
    sp=0
    while sp<=n-i:
        print(" ",end="")
        sp+=1
    ch=0
    while ch<i:
        print(chr(int(ord("A")+ch)),end="")
        ch+=1
    i+=1
    print()
            
