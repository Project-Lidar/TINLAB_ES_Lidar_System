import logging
import asyncio
import ssl
import json

from hbmqtt.client import MQTTClient
from hbmqtt.mqtt.constants import QOS_1, QOS_2


class MqttCommunicator:
    def __init__(self):
        self.C = MQTTClient('Comm_module')  # Initialize the mqtt client

    @asyncio.coroutine
    def send(self, k):
        k = str(k)  # parse input to string

        # connect to mqtt broker
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io')
        tasks = [
            asyncio.ensure_future(
                self.C.publish('sensors/', k.encode(), qos=QOS_2))  # publish message to mqtt broker
        ]
        yield from asyncio.wait(tasks)
        logger.info("messages published")  # logger for development
        yield from self.C.disconnect()  # disconnect from mqtt broker
