def divideGen():
    num = int(input("pick any number between 1 and 100:"))

    if num % 2 == 0 and num % 3 == 0 and num % 5 == 0:
        print(num, " Even and divisible by 3 and 5")
    elif num % 3 == 0 and num % 5 == 0:
        print(num, " Divisible by 3 and 5")
    elif num % 2 == 0 and num % 5 == 0:
        print(num, "Even and divisible by 5")
    elif num % 2 == 0:
        print(num, "Even")
    elif num % 3 == 0:
        print ("Divisible by 3")
    elif num % 5 == 0:
        print(num, " Divisible by 5")
    elif num % 2 == 1:

        print("Odd")


def divisibleBy():
    print("The first number is the number we want to divide. And the second number is the number we want to divide by.")
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    if num1 % num2 == 0:
        print(num1, "is divisible by", num2)
    else:
        print(num1, "is not divisible by", num2)

start = int(input("Welcome to the divisible thingy. if you want to see if a number is odd, even, divisible by 3 or Five press 0. if you want to see if a number is divisible by any other number press 1:"))
if start == 0:
    divideGen()
elif start == 1:
    divisibleBy()

