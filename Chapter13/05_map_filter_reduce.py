from functools import reduce

# Map example
l = [1,2,4,5,6]

square = lambda x:x*x

sqList = map(square,l)
print(list(sqList))

# Filter Example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))


def sum(a,b):
    return a+b
mul = lambda x,y:x*y 

print(reduce(sum,l))
print(reduce(mul,l))