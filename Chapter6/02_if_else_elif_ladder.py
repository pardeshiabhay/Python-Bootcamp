a = int(input("Enter your age: "))
#if else elif ladder
if(a>18):
    print("You are above the age of consent")
    print("Good for you!")
elif(a<0):
    print("You are entering an invalid age")
elif(a==0):
    print("U are entering 0 which is not a valid age")
    
else:
    print("You are below the age of consent")
print("End of the program")