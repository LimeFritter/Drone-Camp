
from typing import final
import Definitions
import random

def userChoice(): 
    userAnswer = input("You have two options from this program. If you want to know how many days are left in the camp type days. if you want to know how long until you are any age type age: ")
    if userAnswer == "age":
        lowerAge = Definitions.lowerAge()
        finalYear = random.randint(lowerAge,100)
        Definitions.ageTo(lowerAge, finalYear)
    elif userAnswer == "days":
        daysLeft = Definitions.campDays()
        print(f"There are {daysLeft} days left.")
    else:
        userChoice()

userChoice()