import random
from easytello import tello
randomBoi = tello.Tello()
vertiTotal = 0
horiTotal = 0
randomBoi.takeoff()
amountLoop = int(input("How many times do you want it to go randomly. \n >>>>      "))
for i in range(amountLoop):
    direction = random.randint(1,4)
    distance = random.randint(20,150)
    if direction == 1:
        if vertiTotal + distance < 210:
            randomBoi.forward(distance)
            print(f"forward, {distance}")
            vertiTotal += distance
        else:
            continue

    elif direction == 2:
        if vertiTotal - distance > -210:
            randomBoi.back(distance)
            print(f"back, {distance}")
            vertiTotal -= distance
        else:
            continue
    elif direction == 3:
        if horiTotal + distance < 150:
            randomBoi.right(distance)
            print(f"right, {distance}")
            horiTotal += distance
        else:
            continue
    elif direction == 4:
        if horiTotal - distance > -150:
            randomBoi.left (distance)
            print(f"left, {distance}")
            horiTotal -= distance
        else:
            continue
randomBoi.go(-vertiTotal,-horiTotal,0,20)



randomBoi.land