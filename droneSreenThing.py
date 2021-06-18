import sys
sys.path.append('/usr/local/lib/python3.9/site-packages')
import getch
from easytello import tello
land = False
keyBoi = tello.Tello()
distance = 50
print("GO!")
while land == False:

    direction =  getch.getch()
    if direction == "i":
        keyBoi.forward(distance)
    elif direction == "k":
        keyBoi.back(distance)
    elif direction == "j":
        keyBoi.left(distance)
    elif direction == "l":
        keyBoi.right(distance)
    elif direction =="w":
        keyBoi.up(distance)
    elif direction == "s":
        keyBoi.down(distance)
    elif direction == "a":
        keyBoi.ccw(45)
    elif direction == "d":
        keyBoi.cw(45)
    elif direction == ".":
        keyBoi.land()
    elif direction == ",":
        keyBoi.takeoff()
    elif direction == "q":
        land = True
    elif direction == "c":
        change = int(input("What is the new distance?"))
        distance = change
keyBoi.land(),