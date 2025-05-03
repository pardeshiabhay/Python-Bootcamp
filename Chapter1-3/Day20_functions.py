# a = 20
# b = 10
# gmean = (a*b)/(a+b)
# print(gmean)

#in function we use (def) keyword

def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")
a=7
b=8
c=9
d=10
calculateGmean(a,b)
isGreater(a,b)
calculateGmean(c,d)
isGreater(c,d)

        
