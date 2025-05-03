countries =("Spain","Italy","India","England","Germany")

temp = list (countries)     #first we have to convert tuple into a list then after time of executing we to change into list into tupple
temp.append("Russia") #aad item
temp.pop(3)           #remove item
temp[2] ="Finland"    #change item
countries = tuple(temp)
print(countries)