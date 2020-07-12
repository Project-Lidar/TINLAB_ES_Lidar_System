import robot.motorControl.motor as motorMovement
import robot.ultrasoon.ultrasoon as collision
import concurrent.futures
import threading

driveTime = 2
minimumDistance = 20

def autoDrive():
    dist = None
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
