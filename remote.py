#import sys
#sys.path.append('/usr/local/lib/python3.9/site-packages')

from easytello import tello 
#import getch

#c = getch.getch()
#print(c)

end = False
myDrone = tello.Tello()

myDrone.takeoff()

while end == False:
    direction = input("what direction do you want? (wasd)\n >>>")
    if direction == "land":
        end = True
        continue
    distance = int(input("how far do you want to go? (cm)\n >>>"))
    
    if 200 < distance or distance < 20:
        if   direction == "w":
            myDrone.forward(25)
        elif direction == "s":
            myDrone.back(25)
        elif direction == "a":
            myDrone.left(25)
        elif direction == "d":
            myDrone.right(25)
       
        continue
    else:
        if direction == "w":
            myDrone.forward(distance)
        elif direction == "s":
            myDrone.back(distance)
        elif direction == "a":
            myDrone.left(distance)
        elif direction == "d":
            myDrone.right(distance)
        else:
            myDrone.forward(25)
myDrone.land()