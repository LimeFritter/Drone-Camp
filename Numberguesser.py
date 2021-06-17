import random
bounds = 0
while bounds == 0:
    lowerBound = int(input("what is the lower bound for guessing: "))
    higherBound = int(input("what is the higher bound for guessing: "))
    if higherBound <= lowerBound:
        print("Sorry that is not a valid answer.")
        continue
    else:
        lowerUseBound = lowerBound
        higherUseBound = higherBound
        compNum = random.randint(lowerBound,higherBound)
        bounds = 1
guess = 0
correct = 0
while correct == 0:
    userWant = input(f"Pick a number {lowerBound}-{higherBound} or type help for help: ")
    
    
    if userWant == "help":
        print("hello. I am the help page. the controls for this game are shown below.\n Control : Function \n help : brings up help page \n bounds : tells you your closest guesses on each side \n quit : stops the program and tells you the answer \n guess : showes the guess you are on")
    elif userWant == "quit":
        print(f"The number was {compNum}")
        correct += 1
    elif userWant == "bounds":
        print(f"the bounds are {lowerUseBound}-{higherUseBound}")
    elif userWant == "guess":
        print(f"you have guessed {guess} times")
    

    else:
        if userWant[:1] == "-":
            userWant[1:].isnumeric()
            guess += 1
            userNum = int(userWant[1:])
            userNum *= -1 
        elif userWant.isnumeric():
            guess += 1
            userNum = int(userWant)
        else:
            print("sorry that is not a valid answer.")
            continue

        if userNum == compNum:
            print(f"Well done. The number was {compNum}. it took you {guess} guesses to figure it out.")
            correct += 1
        elif userNum > compNum:
            print(f"{userNum} is Larger than the number you need")
            if  compNum < userNum < higherUseBound:
                higherUseBound = userNum
        elif userNum < compNum:
            print(f"{userNum} is Smaller than the number you need")
            if  compNum > userNum > lowerUseBound:
                lowerUseBound = userNum
        
    