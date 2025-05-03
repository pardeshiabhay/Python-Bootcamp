'''
1 for snake 
-1 for water
0 for gun
The below logic is written on the basis of the value of computer - you
'''

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict= {"s":1, "w":-1, "g":1}
reverseDict={1:"Snake", -1:"Water", 0:"Gun"}

you = youDict[youstr]

print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")
if(computer == you):
    print("Its a draw")

else:
    if(computer == -1 and you==1):
        print("You win!")
        
    elif(computer == -1 and you == 0):
        print("You Lose!")
        
    elif(computer == 1 and you == -1):
        print("You Lose!")
        
    elif(computer == 1 and you == 0):
        print("You Win!")
        
    elif(computer == 0 and you == -1):
        print("You Win!")
        
    elif(computer == 0 and you == 1):
        print("You Lose!")
        
    else:
        print("Something went wrong:(")
        
