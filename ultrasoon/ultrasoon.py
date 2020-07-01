import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGERL = 29
GPIO_ECHOL = 31
GPIO_TRIGGERR = 32
GPIO_ECHOR = 33
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGERL, GPIO.OUT)
GPIO.setup(GPIO_ECHOL, GPIO.IN)
GPIO.setup(GPIO_TRIGGERR, GPIO.OUT)
GPIO.setup(GPIO_ECHOR, GPIO.IN)
 
def distance_left():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERL, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERL, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHOL) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHOL) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

def distance_right():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGERR, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGERR, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHOR) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHOR) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
