import robot.motorControl.motor as motorMovement
import robot.ultrasoon.ultrasoon as collision
import concurrent.futures
import threading

#time in seconds
driveTime = 2
#distance in centimeters
minimumDistance = 20

def autoDrive():
    dist = None
    #starts a thread where a return function works
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(collision.distance_left())
        dist = future1.result()
    if(dist>minimumDistance):
        threadForward = threading.Thread(target=selfDrivingMovement(True))
        threadForward.start()
    else:
        threadTurn = threading.Thread(target=selfDrivingMovement(False))
        threadTurn.start()

def selfDrivingMovement(free):
    while(free == True):
        motorMovement.drive(driveTime)
    while(free == False):
        motorMovement.turn_left(driveTime)
