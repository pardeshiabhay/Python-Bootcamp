# def average(a,b):
#     print("The average is ", (a+b)/2)

# average(2,4)

# def name(fname,lname):
#     print(fname,lname)
# print("Hey!","Abhay","Pardeshi")

# def name(**name):
#     print("Hello!",name["fname"],name["mname"],name["lname"])
# name(mname="Harish",fname="Abhay",lname="Pardeshi")

def name(*name):
    print("Hello!",name[0],name[1],name[2])
name("Harish","Abhay","Pardeshi")