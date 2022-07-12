n=int(input("Enter anumber:"))
a=n
i=2
while i<a:
    if a%i==0:
        print("Not prime")
        break
    i+=1
else:
        print("Prime")
    
