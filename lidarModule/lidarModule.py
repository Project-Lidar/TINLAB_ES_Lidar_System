import numpy as np
import asyncio
from rplidar import RPLidar
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2

PORT_NAME = 'COM6'


class MqttCommunicator:
    def __init__(self):
        self.C = MQTTClient('Lidar_module')  # Initialize the mqtt client

    @asyncio.coroutine
    def lidarToMqtt(self, data):
        parseData = str(data)
        print(parseData)

        # Connect to mqtt broker
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io')
        tasks = [
            asyncio.ensure_future(
                self.C.publish('lidar/', parseData.encode(), qos=0))  # Publish message to mqtt broker
        ]
        yield from asyncio.wait(tasks)
        yield from self.C.unsubscribe(['lidar/'])
        yield from self.C.disconnect()  # Disconnect from mqtt broker


def scans():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    data = []
    try:
        print('Recording scans... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            data.append(np.array(scan))
            return data

    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()


def measurments():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measurments():
            line = '\t'.join(str(v) for v in measurment)
            return line

    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()
