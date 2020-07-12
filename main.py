import communicationModule.communicationModule as mtq
import time
import motorControl.motorLogic as motor
# import logging
import asyncio
import threading
import socket

mtqq = mtq.MqttCommunicator()

if __name__ == '__main__':
    ## getting the hostname by socket.gethostname() method
    hostname = socket.gethostname()
    print(hostname)
    ## getting the IP address using socket.gethostbyname() method
    ip_address = socket.gethostbyname(hostname)
    print(ip_address)
    # formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    # logging.basicConfig(level=logging.DEBUG, format=formatter)
    # calling send function in communicationModule.py
    # find ipv4 address on arch with command 'ip route show' use the one after 'dhcp src'
    threadipAddr = threading.Thread(target=asyncio.get_event_loop().run_until_complete(mtqq.ipAddr(ip_address)))
    threadipAddr.start()
    threadCamera = threading.Thread(target=mtq.camStream(ip_address, 8000))
    threadCamera.start()

    threadMotor = threading.Thread(target=motor.autoDrive())
    threadMotor.start()

    # Send data to the mqtt broker
    # Get Controller and driving options data from the mqtt broker
    threadController = threading.Thread(target=asyncio.get_event_loop().run_until_complete(mtqq.getController()))
    threadController.start()
    # Send data to the mqtt broker
