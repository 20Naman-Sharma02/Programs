n=int(input("Enter anumber:"))
a=chr(64+n)
i=1
while i<=n:
    j=1
    while j<=i:
        print(chr(int(ord(a)+j-i)),end=" ")
        j+=1
    i+=1
    print()
