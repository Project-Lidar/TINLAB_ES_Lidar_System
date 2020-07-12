import robot.motorControl.manualLogic as manual

#decide where message should go
def messageLogic(topic, message):
    if topic == 'contols/driving/':
        manual.driveState(message)
    else:
        manual.manualControl(topic, message)
