
def campDays():
    campName = input("what is the name of this camp?")

    numDays = int(input(f"How many days are in the {campName}?"))

    currentDay = int(input("What day is it now?"))

    daysLeft = numDays - currentDay
    return daysLeft

def lowerAge():
    lowBound = int(input("How old are you?"))
    return lowBound
def ageTo(lowerYear, finalYear):
    yearsLeft = finalYear - lowerYear
    daysLeft = yearsLeft * 365
    secondLeft = daysLeft * 24 * 60 * 60
    if yearsLeft < 0:
        print(f"You are {yearsLeft * -1} years older than {finalYear}, or {daysLeft * -1:,} days older than {finalYear}, or {secondLeft * -1:,} seconds older than {finalYear}.")
    else:
        print(f"You are {yearsLeft} years until {finalYear}, or {daysLeft:,} days until {finalYear}, or {secondLeft:,} seconds until {finalYear}.")

