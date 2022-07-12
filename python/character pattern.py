
n=int(input("Enter anumber:"))
i=0
while i<=n:
    j=0
    while j<=i:
        print(chr(int(ord("A")+j)),end=" ")
        j+=1
    i+=1
    print()
