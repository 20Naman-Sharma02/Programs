n=int(input("Enter a number:"))
i=0
while i<n:
    j=0
    while j<=i:
        print(chr(int(ord("A")+i)),end=" ")
        j=j+1
    i+=1
    print()
