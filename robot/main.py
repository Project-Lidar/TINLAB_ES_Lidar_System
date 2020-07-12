import communicationModule.communicationModule as mtq
import time
import motorControl.motorLogic as motor
import asyncio
import threading
import socket

mtqq = mtq.MqttCommunicator()

if __name__ == '__main__':
    #getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    print(hostname)
    #getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    
    #send IP for camera stream to webapp
    threadipAddr = threading.Thread(target=asyncio.get_event_loop().run_until_complete(mtqq.ipAddr(ip_address)))
    threadipAddr.start()
    #start camera stream
    threadCamera = threading.Thread(target=mtq.camStream(ip_address, 8000))
    threadCamera.start()

    threadMotor = threading.Thread(target=motor.autoDrive())
    threadMotor.start()

    # Get Controller and driving options data from the mqtt broker
    threadController = threading.Thread(target=asyncio.get_event_loop().run_until_complete(mtqq.getController()))
    threadController.start()
