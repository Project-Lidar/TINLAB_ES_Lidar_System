import numpy as np
import asyncio
import time
import communicationModule.communicationModule as comm
from rplidar import RPLidar

PORT_NAME = '/dev/ttyACM0'

mqtt = comm.MqttCommunicator()

# Publishes lists of the RPlidar A1 measurements


def scans():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    data = []
    try:
        print('Recording scans... Press Crl+C to stop.')
        for scan in lidar.iter_scans():
            data.append(np.array(scan))
            # ensures that the publish rate does not exceed shiftr.io dynamic rate limit (25 messages/sec)
            time.sleep(0.05)
            asyncio.get_event_loop().run_until_complete(mqtt.lidarToMqtt(scan))

    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()


# Publishes the RPlidar A1 measurements


def measurments():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    try:
        print('Recording measurments... Press Crl+C to stop.')
        for measurment in lidar.iter_measurments():
            line = '\t'.join(str(v) for v in measurment)
            # ensures that the publish rate does not exceed shiftr.io dynamic rate limit (25 messages/sec)
            time.sleep(0.05)
            asyncio.get_event_loop().run_until_complete(mqtt.postLidar(line))

    except KeyboardInterrupt:
        print('Stoping.')
    lidar.stop()
    lidar.disconnect()