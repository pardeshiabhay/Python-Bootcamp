class Demo:
    a = 4

#Prints the class attribute because instance attribute is not present
o = Demo()
print(o.a)

#Instance attribute is set it prints the instance attribute because it is present
o.a = 0
print(o.a)

#Prints the class attribute
print(Demo.a)

#answer is the class attribute did not change