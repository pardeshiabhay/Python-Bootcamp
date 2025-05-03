'''
1 for snake 
-1 for water
0 for gun
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
    if((computer - you)== -1 or (computer -you)== 2):
        print("You Lose! :(")
    else:
        print("You Win! :)")