n=int(input("Enter a number"))
i=1
a=n//2
while i<=n:
    sp=0
    while sp<=n-i:
        print(" ",end="")
        sp+=1
        '''the above code is for spaces in triangle'''
    
    st=0
    while st<i:
        print("*",end="")
        st+=1
    st2=i-1
    while st2>=1:
        print("*",end="")
        st2-=1
        '''the above code will print stars'''
    i+=1
    print()

    """Above code is for triangle"""
        
i=n-1
while i<n:
    if i==-1:
        break
    sp=0
    while sp<=n-i:
         print(" ",end="")
         sp+=1
         '''the above code is for spaces in inverted triangke'''
    st=0
    while st<i:
        print("*",end="")
        st+=1
    st2=1
    while st2<i:
        print("*",end="")
        st2+=1
        '''the above code will print stars'''
    i-=1
    print()
    """Above code is for inverted traingle"""

