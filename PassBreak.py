#you can type anynumber of any length and this will guess it
import time
play = True
while play == True: 
    password = input("type any number\n >>>>   ")
    passLength = len(password)
    passToGuess = []
    compguess = []
    compfinal = []
    for q in range(passLength):
        passToGuess.append(int(password[q]))
    compguess = [0] * passLength
    compfinal = [0] * passLength

    x = 0
    for x in range(passLength):

        i=0
        for i in range (10):
            
            time.sleep(0.1)
            compguess[x] = i
            print(compguess)
            if compguess[x] == passToGuess[x]:
                compfinal[x] = compguess[x]
                break
                
    compNice = str(compfinal)
    print(f"{compNice} got it")
    playAgain = input("type y to play again or n to stop. \n >>>   ")
    if playAgain == "y":
        play = True
    else:
        play = False
        print("Thanks for playing")
