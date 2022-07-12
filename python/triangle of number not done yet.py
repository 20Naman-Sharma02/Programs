n=int(input("Enter a anumber:"))
for i in range(1,n+1,1):
    for s in range(n-i):
        print(" ",end="")
    for num in range(i,2*i,1):
        print(num,end="")
    for num in range(2*i-2,i-1,-1):
        print(num,end="")
    print()
