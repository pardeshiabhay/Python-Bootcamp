# c = 5*(f-32)/9
#normal 
# f = int(input("Enter temperature in F: "))
# c = 5*(f-32)/9
# print(c)

#by using function
def f_to_c(f):
    return 5*(f-32)/9

f= int(input("Enter temperature in F: "))
c= f_to_c(f)

print(f"{round(c,2)}°C")