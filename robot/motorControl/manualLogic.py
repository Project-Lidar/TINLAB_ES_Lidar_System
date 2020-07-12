import robot.motorControl.motor as motor
import robot.motorControl.motorLogic as logic
import robot.ultrasoon.ultrasoon as collision
import concurrent.futures

minimumDistance = 20

def driveState(state):
    if state == 'A':
        logic.autoDrive()
    elif state == 'M':
        manualControl()

def manualControl(movement, direction):
    dist = None
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(collision.distance_left())
        dist = future1.result()
    if(dist<minimumDistance):
        motor.stop()
    elif direction == 'D':
        motor.drive()
    elif direction == 'B':
        motor.stop()
    elif direction == 'L':
        motor.turn_left()
    elif direction == 'R' and movement == 'controls/manual/controller/speed':
        motor.reverse()
    elif direction == 'R' and movement == 'controls/manual/controller/steer':
        motor.turn_right()

