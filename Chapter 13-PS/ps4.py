def  div5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,45678,54678,67895,65,78,45,55]

f = list(filter(div5, a))
print(f)