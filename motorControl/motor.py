#forward -> check ultrasonic
#Go right -> check lidar
#Go Left -> check lidar
#Go back -> Turn -> check lidar -> don't turn -> check lidar
import l293d.driver as l293d
import time

motorR1 = l293d.DC(3,5,7)
motorR2 = l293d.DC(36,38,40)
motorR3 = l293d.DC(11,13,15)
motorL1 = l293d.DC(12,16,18)
motorL2 = l293d.DC(19,21,23)
motorL3 = l293d.DC(22,24,26)

def drive(duration):
    motorL1.clockwise(speed=(40,100))
    motorL2.clockwise(speed=(40,100))
    motorL3.clockwise(speed=(40,100))
    motorR1.anticlockwise(speed=(40,100))
    motorR2.anticlockwise(speed=(40,100))
    motorR3.anticlockwise(speed=(40,100))
    time.sleep(duration)

def reverse(duration):
    motorL1.anticlockwise(speed=(40,100))
    motorL2.anticlockwise(speed=(40,100))
    motorL3.anticlockwise(speed=(40,100))
    motorR1.clockwise(speed=(40,100))
    motorR2.clockwise(speed=(40,100))
    motorR3.clockwise(speed=(40,100))
    time.sleep(duration)

def turn_right(duration):
    motorL1.anticlockwise(speed=(40,100))
    motorL2.anticlockwise(speed=(40,100))
    motorL3.anticlockwise(speed=(40,100))
    motorR1.anticlockwise(speed=(40,100))
    motorR2.anticlockwise(speed=(40,100))
    motorR3.anticlockwise(speed=(40,100))
    time.sleep(duration)

def turn_left(duration):
    motorL1.clockwise(speed=(40,100))
    motorL2.clockwise(speed=(40,100))
    motorL3.clockwise(speed=(40,100))
    motorR1.clockwise(speed=(40,100))
    motorR2.clockwise(speed=(40,100))
    motorR3.clockwise(speed=(40,100))
    time.sleep(duration)

def park():
    l293d.cleanup()

def stop():
    motorL1.stop()
    motorL2.stop()
    motorL3.stop()
    motorR1.stop()
    motorR2.stop()
    motorR3.stop()
