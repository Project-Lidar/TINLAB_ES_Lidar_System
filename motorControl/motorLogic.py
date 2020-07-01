import motorControl.motor as motorMovement
import ultrasoon.ultrasoon as collision
import concurrent.futures

distR = None
distL = None
freeL = False
freeR = False

def __init__(self):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(collision.distance_right())
        future1 = executor.submit(collision.distance_left())
        distR = future.result()
        distL = future1.result()
    if(distL>20):
        freeL=True
    else:
        freeL=False
    if (distR>20):
        freeR=True
    else:
        freeR=False
    selfDrivingMovement()

def selfDrivingMovement():
    while(freeL and freeR):
        motorMovement.drive(1)
