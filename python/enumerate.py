for i in range(5):
    number = int(input("Please Enter any Number: "))
    r = 0
    a = number
    while(a > 0):
        Reminder = a % 10
        r = (r * 10) + Reminder
        a = a //10
    if number==r:
       print("pallindrome")
    else:
       print("Not pallindrome")
    
