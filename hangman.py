from typing import NewType


def wrong1():   
    print(" ----- \n |   | \n |    \n |   \n |   \n/|\ \n---")
def wrong2():
    print(" ----- \n |   | \n |   0 \n |  \n |   \n/|\ \n---")
def wrong3():
    print(" ----- \n |   | \n |   0 \n |  /|\  \n |   \n/|\ \n---")
def wrong4():
    print(" ----- \n |   | \n |   0 \n |  /|\ \n |   /\ \n/|\ \n---")

toBeGuess = input("what is the word being guessed? \n >>> ")
for y in range(100):
    print("\n")
blank = len(toBeGuess)
userSee = ""
win = False
loss = 0
safe = False
letters = ""
for i in range(blank):
    if toBeGuess[i].isalpha():
        userSee += "_"
    else:
        userSee += toBeGuess[i]

while win == False:
    safe = False
    userGuess = input(f"Guess a letter.{userSee} \n>>>  ")
    newUserSee =""
    if userGuess == "letters":
            print(letters)
            safe = True
            continue
    elif userGuess == "exit":
        print(f"the word was {toBeGuess}")
        win = True
        continue
    for x in range(blank):
        if userGuess == f"{toBeGuess[x]}":
            newUserSee += f"{userGuess}"
            safe = True
        
        
        else:
            newUserSee += userSee[x] 

    userSee = newUserSee
    if userSee == toBeGuess:
        print(f"You Win!\n The Word Was:\n {toBeGuess}")
        win = True
    if safe == False:
        loss += 1
        print(f"{userGuess} is not correct")
        if loss == 1:
            wrong1()
        elif loss == 2:
            wrong2()

        elif loss == 3:
            wrong3()

        elif loss == 4:
            wrong4()
            print("Game Over.")
            win = True
    letters += f" {userGuess}"
    
    

        
            
