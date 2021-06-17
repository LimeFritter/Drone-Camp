from easytello import tello
stairBoi = tello.Tello()
stairBoi.takeoff()
firstGround = int(stairBoi.get_tof())
height = stairBoi.get_height()
print(f"{height}")
stair = 1
while stair == 1: 
    nowGround = stairBoi.get_tof()
    fromGround= firstGround - nowGround
    print(f"now:{nowGround} Change: {fromGround}")
    print(fromGround)
    if -10<= fromGround <= 10:
     stairBoi.forward(25)
    elif -10 > fromGround > 10:
        checkHeight = stairBoi.get_tof()
        if fromGround > 0:
            if  checkHeight < 800:
                stairBoi.go(0,0,800-checkHeight,20)
            
            else:
                stairBoi.go(0,0,checkHeight-800,20)
        else:
            if  checkHeight < 50:
                stairBoi.go(0,0,checkHeight - 800,20)
            
            else:
                stairBoi.go(0,0,checkHeight,20)



        
    
            

    


    
    

