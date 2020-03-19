import communicationModule.communicationModule as mtq
import time
#import logging
import asyncio

mtqq = mtq.MqttCommunicator()

if __name__ == '__main__':
    formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    #logging.basicConfig(level=logging.DEBUG, format=formatter)
    # calling send function in communicationModule.py
    #find ipv4 address on arch with command 'ip route show' use the one after 'dhcp src'
    mtq.camStream('192.168.2.19',8000)
    asyncio.get_event_loop().run_until_complete(mtqq.send('#RIP'))
    asyncio.get_event_loop().run_until_complete(mtqq.receive())
    asyncio.get_event_loop().run_until_complete(mtqq.send('#LIFE'))
