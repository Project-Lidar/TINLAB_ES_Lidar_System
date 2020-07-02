import motorControl.motor as motorMovement
import ultrasoon.ultrasoon as collision
import concurrent.futures

distR = None
distL = None
freeL = False
freeR = False
minimumDistance = 20

def __init__(self):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(collision.distance_right())
        future1 = executor.submit(collision.distance_left())
        distR = future.result()
        distL = future1.result()
    if(distL>minimumDistance):
        freeL=True
    else:
        freeL=False
    if (distR>minimumDistance):
        freeR=True
    else:
        freeR=False
    selfDrivingMovement()

def selfDrivingMovement():
    while(freeL and freeR):
        motorMovement.drive(1)
    while(freeL and not freeR):
        motorMovement.turn_left()
    while(not freeL and freeR):
        motorMovement.turn_right()
    while(not freeL and not freeR):
        motorMovement.reverse()
