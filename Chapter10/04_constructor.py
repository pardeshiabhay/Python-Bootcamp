class employee:
    language = "Python"   #This is  class attribute
    salary = 1200000
    
    def __init__(self, name, salary,language):   # dunder method is automatically called
        self.name = name
        self.salary = salary
        self.language =language
        print("I am creating an object")
    
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")
    
abhay = employee("Abhay",1300000,"JavaScript")
#abhay.name ="Abhay"       #This is an instance attribute
#employee.getInfo(abhay)
#amaan = employee()
print(abhay.name, abhay.salary, abhay.language)
