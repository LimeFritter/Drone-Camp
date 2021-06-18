from easytello import tello
steve = tello.Tello()
def liftoff():
    steve.takeoff()

def horiSquare():

    for i in range(4):
        steve.forward(40)
        steve.cw(90)
    

def vertiSquare():
    steve.up(60)
    steve.back(60)
    steve.down(60)
    steve.forward(60)
def battCheck():
    print(steve.get_battery)
def circle():
    for i in range (12):
        steve.cw(30)
        steve.left(40)
def vertiCircle():
    steve.curve(50,50,0,-50,0,30,20)
    steve.curve(50,50,0,70,0,-30,20)

steve.takeoff()
#steve.go(50,50,50,30)
#steve.go(50,-50,-50,30)

#steve.forward(100)

#steve.curve(50,50,0,50,-50,0,30)
#vertiCircle()
#steve.flip("b")
#steve.land()
vertiSquare()



