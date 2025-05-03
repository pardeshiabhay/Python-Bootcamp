x= int(input("Enter the value of x: "))
#x is variable to match

match x:
    #if x is 0
    case 0:
        print("x is zero")
    # case with if condition
    case 4:
        print("case is 4")
        
    case _:
        print(x)