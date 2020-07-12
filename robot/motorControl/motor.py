import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#ports for motors
motorR1A = 7
motorR1B = 11
motorR2A = 12
motorR2B = 13
motorR3A = 15
motorR3B = 16
motorL1A = 18
motorL1B = 22
motorL2A = 29
motorL2B = 31
motorL3A = 32
motorL3B = 33

GPIO.setup(motorR1A, GPIO.OUT)
GPIO.setup(motorR1B, GPIO.OUT)
GPIO.setup(motorR2A, GPIO.OUT)
GPIO.setup(motorR2B, GPIO.OUT)
GPIO.setup(motorR3A, GPIO.OUT)
GPIO.setup(motorR3B, GPIO.OUT)
GPIO.setup(motorL1A, GPIO.OUT)
GPIO.setup(motorL1B, GPIO.OUT)
GPIO.setup(motorL2A, GPIO.OUT)
GPIO.setup(motorL2B, GPIO.OUT)
GPIO.setup(motorL3A, GPIO.OUT)
GPIO.setup(motorL3B, GPIO.OUT)

def drive(duration):
    GPIO.output(motorR1A, GPIO.LOW)
    GPIO.output(motorR1B, GPIO.HIGH)
    GPIO.output(motorR2A, GPIO.LOW)
    GPIO.output(motorR2B, GPIO.HIGH)
    GPIO.output(motorR3A, GPIO.LOW)
    GPIO.output(motorR3B, GPIO.HIGH)
    GPIO.output(motorL1A, GPIO.HIGH)
    GPIO.output(motorL1B, GPIO.LOW)
    GPIO.output(motorL2A, GPIO.HIGH)
    GPIO.output(motorL2B, GPIO.LOW)
    GPIO.output(motorL3A, GPIO.HIGH)
    GPIO.output(motorL3B, GPIO.LOW)
    time.sleep(duration)

def reverse(duration):
    GPIO.output(motorR1A, GPIO.HIGH)
    GPIO.output(motorR1B, GPIO.LOW)
    GPIO.output(motorR2A, GPIO.HIGH)
    GPIO.output(motorR2B, GPIO.LOW)
    GPIO.output(motorR3A, GPIO.HIGH)
    GPIO.output(motorR3B, GPIO.LOW)
    GPIO.output(motorL1A, GPIO.LOW)
    GPIO.output(motorL1B, GPIO.HIGH)
    GPIO.output(motorL2A, GPIO.LOW)
    GPIO.output(motorL2B, GPIO.HIGH)
    GPIO.output(motorL3A, GPIO.LOW)
    GPIO.output(motorL3B, GPIO.HIGH)
    time.sleep(duration)

def turn_right(duration):
     GPIO.output(motorR1A, GPIO.HIGH)
    GPIO.output(motorR1B, GPIO.LOW)
    GPIO.output(motorR2A, GPIO.HIGH)
    GPIO.output(motorR2B, GPIO.LOW)
    GPIO.output(motorR3A, GPIO.HIGH)
    GPIO.output(motorR3B, GPIO.LOW)
    GPIO.output(motorL1A, GPIO.HIGH)
    GPIO.output(motorL1B, GPIO.LOW)
    GPIO.output(motorL2A, GPIO.HIGH)
    GPIO.output(motorL2B, GPIO.LOW)
    GPIO.output(motorL3A, GPIO.HIGH)
    GPIO.output(motorL3B, GPIO.LOW)
    time.sleep(duration)

def turn_left(duration):
    GPIO.output(motorR1A, GPIO.LOW)
    GPIO.output(motorR1B, GPIO.HIGH)
    GPIO.output(motorR2A, GPIO.LOW)
    GPIO.output(motorR2B, GPIO.HIGH)
    GPIO.output(motorR3A, GPIO.LOW)
    GPIO.output(motorR3B, GPIO.HIGH)
    GPIO.output(motorL1A, GPIO.LOW)
    GPIO.output(motorL1B, GPIO.HIGH)
    GPIO.output(motorL2A, GPIO.LOW)
    GPIO.output(motorL2B, GPIO.HIGH)
    GPIO.output(motorL3A, GPIO.LOW)
    GPIO.output(motorL3B, GPIO.HIGH)
    time.sleep(duration)

def park():
    GPIO.cleanup()

def stop():
    GPIO.output(motorR1A, GPIO.LOW)
    GPIO.output(motorR1B, GPIO.LOW)
    GPIO.output(motorR2A, GPIO.LOW)
    GPIO.output(motorR2B, GPIO.LOW)
    GPIO.output(motorR3A, GPIO.LOW)
    GPIO.output(motorR3B, GPIO.LOW)
    GPIO.output(motorL1A, GPIO.LOW)
    GPIO.output(motorL1B, GPIO.LOW)
    GPIO.output(motorL2A, GPIO.LOW)
    GPIO.output(motorL2B, GPIO.LOW)
    GPIO.output(motorL3A, GPIO.LOW)
    GPIO.output(motorL3B, GPIO.LOW)
