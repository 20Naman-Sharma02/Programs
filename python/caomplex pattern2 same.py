n=int(input("Enter a number:"))
print("*" * n,end="\n")
i=(n//2)-1
j=2
while i!=0:
    while j<=(n-2):
        print("*" *i,end="")
        print("_"*j,end="")
        print("*" *i,end="\n")
        i=i-1
        j=j+2
