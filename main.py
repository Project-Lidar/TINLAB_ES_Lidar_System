import communicationModule.communicationModule as mtq
import time

mtq1 = mtq.MqttCommunicator()

while True:
    mtq1.send()
    time.sleep(0.2)