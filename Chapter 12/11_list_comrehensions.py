myList = [1,2,3,5,7,9]

# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

#Easy way to do with List comprehensions
squaredList = [i*i for i in myList]

print(squaredList)