class employee:
    language = "Python"   #This is  class attribute
    salary = 1200000
    
    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning!")
    
abhay = employee()
abhay.name ="Abhay"       #This is an instance attribute
abhay.greet()
abhay.getInfo()
#employee.getInfo(abhay)
