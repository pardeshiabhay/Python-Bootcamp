#implement the table in reverse format
n= int(input("Enter the number: "))
for i in range(1,11):
    print(f"{n}x{11-i} = {n * (11-i)}")
    