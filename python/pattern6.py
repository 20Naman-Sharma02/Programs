
n=int(input("Enter a number:"))
i=1
for i in range (1,n+1):
    j=1
    for j in range(1,i+1):
        print(i,end=" ")
        j=j+1
    i+=1
    print()
