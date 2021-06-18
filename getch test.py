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
    if direction == "w":
        keyBoi.forward(distance)
    elif direction == "s":
        keyBoi.back(distance)
    elif direction == "a":
        keyBoi.left(distance)
    elif direction == "d":
        keyBoi.right(distance)
    elif direction ==".":
        keyBoi.up(distance)
    elif direction == ",":
        keyBoi.down(distance)
    elif direction == "l":
        keyBoi.land()
    elif direction == "t":
        keyBoi.takeoff()
    elif direction == "q":
        land = True
    elif direction == "c":
        change = int(input("What is the new distance?"))
        distance = change
keyBoi.land()
    
