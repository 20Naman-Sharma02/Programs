n=int(input("Enteter anumber:"))
i=1
j=1
while i<=n:
    if i%2!=0:
        while j<=i:
            print("*",end="")
            j=j+1
    elif i%2==0:
        while j<=n:
            print(i-1,end="")
            j=j+1
    i=+1
                        
            

            
        
    
