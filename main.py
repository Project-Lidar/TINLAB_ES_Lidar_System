import communicationModule.communicationModule as mtq
import time
import logging
import asyncio

mtqq = mtq.MqttCommunicator()

if __name__ == '__main__':
    formatter = "[%(asctime)s] %(name)s {%(filename)s:%(lineno)d} %(levelname)s - %(message)s"
    logging.basicConfig(level=logging.DEBUG, format=formatter)
    # calling send function in communicationModule.py
    asyncio.get_event_loop().run_until_complete(mtqq.send('sensor_input'))
