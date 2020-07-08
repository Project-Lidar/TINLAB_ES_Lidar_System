import motorControl.motor as motorMovement
import ultrasoon.ultrasoon as collision
import concurrent.futures

distL = None
freeL = False
minimumDistance = 20
driveTime = 2

def __init__(self):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(collision.distance_left())
        distL = future1.result()
    if(distL>minimumDistance):
        freeL=True
    else:
        freeL=False
    selfDrivingMovement()

def selfDrivingMovement():
    while(freeL):
        motorMovement.drive(driveTime)
    while(not freeL):
        motorMovement.turn_left(driveTime)
