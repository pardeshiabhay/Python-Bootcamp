from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self,fro,to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    
    def getFare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(444,6666)}")

t = Train(23765)
t.book("Mumbai","Goa")
t.getStatus()
t.getFare("Mumbai","Goa")