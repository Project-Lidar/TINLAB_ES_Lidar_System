import asyncio
import ssl
import json
import threading
import socket
import argparse
import unittest
import datetime
import imutils
import time
import cv2
import logging
import cameraModule.cameraModule as cam
import communicationModule.receiveMessage as getMessage

from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2


class MqttCommunicator:
    #@asyncio.coroutine
    def __init__(self):
        self.C = MQTTClient('Comm_module')  # Initialize the mqtt client

    @asyncio.coroutine
    def ipAddr(self, k):
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io')
        tasks = [
            asyncio.ensure_future(
                self.C.publish('ipAddress/', k.encode(), qos=0))  # Publish message to mqtt broker
        ]
        yield from asyncio.wait(tasks)
        # logger.info("messages published")  # Logger for development
        # Unsubscribe from topic before disconnect
        yield from self.C.unsubscribe(['ipAddress/'])
        yield from self.C.disconnect()  # Disconnect from mqtt broker

    @asyncio.coroutine
    def send(self, k):
        k = str(k)  # Parse input to string

        # Connect to mqtt broker
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io')
        tasks = [
            asyncio.ensure_future(
                self.C.publish('sensors/', k.encode(), qos=0))  # Publish message to mqtt broker
        ]
        yield from asyncio.wait(tasks)
        # logger.info("messages published")  # Logger for development
        # Unsubscribe from topic before disconnect
        yield from self.C.unsubscribe(['sensors/'])
        yield from self.C.disconnect()  # Disconnect from mqtt broker

    # Publish lidar data
    @asyncio.coroutine
    def postLidar(self, data):
        parseData = str(data)

        # Connect to mqtt broker
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io')
        tasks = [
            asyncio.ensure_future(
                self.C.publish('lidar/', parseData.encode(), qos=0))  # Publish message to mqtt broker
        ]
        yield from asyncio.wait(tasks)
        yield from self.C.unsubscribe(['lidar/'])
        yield from self.C.disconnect()  # Disconnect from mqtt broker

    @asyncio.coroutine
    def getController(self):
        # connect to mqtt broker
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io/')
        yield from self.C.subscribe([
            # Subscribed to speed topic
            ('controls/manual/controller/speed', QOS_0),
            # Subscribed to steer topic
            ('controls/manual/controller/steer', QOS_0),
            # Subscribed to driving topic
            ('controls/driving/', QOS_0),
        ])
        print('hello')
        try:
            # Wait for 100 inputs from the broker before disconnecting and unsubscribing from the broker (for test/dev purposes)
            i=0
            while(True):
                message = yield from self.C.deliver_message()
                packet = message.publish_packet
                print('k')
                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(packet.payload.data)))
                getMessage.messageLogic(packet.variable_header.topic_name, str(packet.payload.data).decode())
                i=i+1
            yield from self.C.unsubscribe(['controls/manual/controller/speed', 'controls/manual/controller/steer', 'contols/driving/'])
            yield from self.C.disconnect()
        except ClientException as ce:
            print(ce)
            #logger.error("Client exception: %s" % ce)


def camStream(ip, port):
    # start a thread that will perform motion detection
    t = threading.Thread(target=cam.detect_motion, args=(64,))
    t.daemon = True
    t.start()

    # start the flask app
    threadSend = threading.Thread(target=cam.app.run(host=ip, port=port, debug=True,
                threaded=True, use_reloader=False))#ssl_context='adhoc',
    threadSend.start()