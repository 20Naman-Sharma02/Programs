n=int(input())
i=0
a=n//2
r=n%2
if a==1:
    pass
while i<=a:
    j=0
    while j<=i:
        print(" ",end="")
        j+=1
    st=0
    while st<=i:
        print("*",end="")
        st+=1
    i+=1
    print()
i=(n-a)
while i>=1:
    j=1
    while j<=i:
        print(" ",end="")
        j+=1
    st=1
    while st<=i:
        print("*",end="")
        st+=1
    i-=1
    print()
