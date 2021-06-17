from easytello import tello
racer = tello.Tello()
front = 170
side = 150
def rightChair():
    racer.forward(front)
    racer.right(side)
def leftChair():
    racer.forward(front)
    racer.left(side)
racer.takeoff()

racer.right(80)
leftChair()
rightChair()
leftChair()
racer.ccw(180)
racer.right(60)
leftChair()
rightChair()
racer.forward(50)
racer.left(80)
racer.land()