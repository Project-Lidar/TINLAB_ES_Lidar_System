import controllerModule.controllerModule as mtq
import time
import asyncio

mtqq = mtq.MqttCommunicator()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(mtqq.getController())
