import random
comp1 = random.randint(1,9)
comp2 = random.randint(1,9)
comp3 = random.randint(1,9)
comp4 = random.randint(1,9)
comp5 = random.randint(1,9)
compNum = f"{comp1}{comp2}{comp3}{comp4}{comp5}"
#print(f"{compNum}") #this is here for ease of testing
win = 0
highest = 0
highComp = 0
guess = 1
print("The number has been chosen")
while win == 0:
    compResponse = [0,0,0,0,0]
    sumBest = 0
    now = [0,0,0,0,0]

    userNum = input("guess any 5 digit number or type help.")
    if userNum == "help":
        print("This is the help page. the keywords for this game are: rules, this brings up the rules page. help, this brings up the help page. close, this brings up your closest guess. quit, gives up and gives you the answer ")
    elif userNum == "rules":
        "The rules of this game are simple. the computer will generate a 5 digit number. you will then guess a five digit number. if you have a digit that is not in the computors number the computer will print a 0 in its place. if you have a digit that is correct but not in the right position the computer will print a 1 in its place. If you have a digit that is in the correct position then the computer will print a 2. you only have ten guesses to finish the game"
    elif userNum == "close":
        if highest == 0:
            print("you do not have a closest guess")
        else:
            print(f"{highest} \n {highComp}")
    elif userNum == "quit":
        print(f"You Lose. The answer was {compNum}")
        win += 1
    else:
        if userNum.isnumeric():
            userNumlist = [int(userNum[0]),int(userNum[1]),int(userNum[2]),int(userNum[3]),int(userNum[4])]
            guess += 1

            if userNumlist[0] == int(comp1):
                compResponse[0] = 2
            elif userNumlist[0] != comp1:
                if userNumlist[0] == comp2:
                    compResponse[0] = 1
                elif userNumlist[0] == comp3:
                    compResponse[0] = 1
                elif userNumlist[0] == comp4:
                    compResponse[0] = 1
                elif userNumlist[0] == comp5:
                    compResponse[0] = 1
                else:
                    compResponse[0] = 0
            
            if userNumlist[1] == int(comp2):
                compResponse[1] = 2
            elif userNumlist[1] != comp2:
                if userNumlist[1] == comp1:
                    compResponse[1] = 1
                elif userNumlist[1] == comp3:
                    compResponse[1] = 1
                elif userNumlist[1] == comp4:
                    compResponse[1] = 1
                elif userNumlist[1] == comp5:
                    compResponse[1] = 1
                else:
                    compResponse[0] = 0

                    
            if userNumlist[2] == comp3:
                compResponse[2] = 2
            elif userNumlist[2] != comp3:
                if userNumlist[2] == comp1:
                    compResponse[2] = 1
                elif userNumlist[2] == comp2:
                    compResponse[2] = 1
                elif userNumlist[2] == comp4:
                    compResponse[2] = 1
                elif userNumlist[2] == comp5:
                    compResponse[2] = 1
                else:
                    compResponse[2] = 0
            if userNumlist[3] == comp4:
                compResponse[3] = 2
            elif userNumlist[3] != comp4:
                if userNumlist[3] == comp1:
                    compResponse[3] = 1
                elif userNumlist[3] == comp2:
                    compResponse[3] = 1
                elif userNumlist[3] == comp3:
                    compResponse[3] = 1
                elif userNumlist[3] == comp5:
                    compResponse[3] = 1
                else:
                    compResponse[3] = 0
            if userNumlist[4] == comp5:
                compResponse[4] = 2
            elif userNumlist[4] != comp5:
                if userNumlist[4] == comp1:
                    compResponse[4] = 1
                elif userNumlist[4] == comp2:
                    compResponse[4] = 1
                elif userNumlist[4] == comp3:
                    compResponse[4] = 1
                elif userNumlist[4] == comp4:
                    compResponse[4] = 1
                else:
                    compResponse[4] = 0
            print(f"{compResponse[0]}{compResponse[1]}{compResponse[2]}{compResponse[3]}{compResponse[4]}")
            now[0] = compResponse[0]
            now[1] = compResponse[1]
            now[2] = compResponse[2]
            now[3] = compResponse[3]
            now[4] = compResponse[4]
            if now[0] + now[1] + now[2] + now[3] + now[4] > int(highest):
                highest = f"{userNumlist[0]}{userNumlist[1]}{userNumlist[2]}{userNumlist[3]}{userNumlist[4]}"
                highComp = f"{compResponse[0]}{compResponse[1]}{compResponse[2]}{compResponse[3]}{compResponse[4]}"
            
            if now[0] + now[1] + now[2] + now[3] + now[4] == 10:
                print(f"you win!!! The number was {compNum} it took {guess} tries")
                win += 1
            else:
                continue
        
        else:
            continue
