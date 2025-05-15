from functools import reduce
l = [111,25,783,54,95,65,78,45,55]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))