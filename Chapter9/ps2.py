import random

def game():
    print("You are playing the game... ")
    score =random.randint( 1, 100)
    
    #fetch the highscore
    with open("highscore.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0
            
    print(f"Your score: {score}")
    if(score>hiscore):
        #write this hiscore to the file
        with open("highscore.txt", "w") as f:
            f.write(str(score))
            
    return score
game()