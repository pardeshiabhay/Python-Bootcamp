class employee:
    language = "Python"   #This is  class attribute
    salary = 1200000
    
abhay = employee()
abhay.name ="Abhay"       #This is an instance attribute
print(abhay.name,abhay.language, abhay.salary)

amaan = employee()
amaan.name = "Ammaan Jackson"
print(amaan.name,amaan.language,amaan.salary)

'''
name is instance attribute and salary and language
are class attribute as they are directly belong to the classhere
'''
