
def campDays():
    campName = input("what is the name of this camp?")

    numDays = int(input(f"How many days are in the {campName}?"))

    currentDay = int(input("What day is it now?"))

    daysLeft = numDays - currentDay

    print(f"There are {daysLeft} days left.")

def ageTo30():
    currentAge = int(input("how old are you now? "))
    yearsLeft = 30 - currentAge
    daysLeft = yearsLeft * 365
    secondLeft = daysLeft * 24 * 60 * 60
    print(f"You are {yearsLeft} years from being 30, or {daysLeft:,} days from being 30, or {secondLeft:,} seconds until you are 30.")

def userChoice(): 
    userAnswer = input("You have two options from this program. If you want to know how many days are left in the camp type days. if you want to know how long until you are 30 type age: ")
    if userAnswer == "age":
        ageTo30()
    elif userAnswer == "days":
        campDays()
    else:
        userChoice()


userChoice()