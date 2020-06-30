import lidarModule.lidarModule as lidar
import time
import asyncio

mqtt = lidar.MqttCommunicator()

if __name__ == '__main__':
    data = lidar.scans()
    # data = lidar.measurments()
    asyncio.get_event_loop().run_until_complete(mqtt.lidarToMqtt(data))
