import asyncio
import logging
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_1, QOS_2


class MqttCommunicator:
    def __init__(self):
        self.C = MQTTClient('Comm_module')  # Initialize the mqtt client

    @asyncio.coroutine
    def getController(self):
        # connect to mqtt broker
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io/')
        yield from self.C.subscribe([
            ('controls/manual/controller/', QOS_2),
            ('controls/driving/', QOS_2),
        ])
        try:
            for i in range(1, 100):
                message = yield from self.C.deliver_message()
                packet = message.publish_packet
                print("%d:  %s => %s" % (
                    i, packet.variable_header.topic_name, str(packet.payload.data)))
            yield from self.C.unsubscribe(['controls/manual/controller/', 'contols/driving/'])
            yield from self.C.disconnect()
        except ClientException as ce:
            logger.error("Client exception: %s" % ce)
