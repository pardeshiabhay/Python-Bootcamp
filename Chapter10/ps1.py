class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = Programmer("Abhay",1300000,401107)
print(p.name,p.salary,p.pin,p.company   )
        