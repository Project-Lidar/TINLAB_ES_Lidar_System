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
import cameraModule.cameraModule as cam

from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template
from hbmqtt.client import MQTTClient, ClientException
from hbmqtt.mqtt.constants import QOS_0, QOS_1, QOS_2

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
                self.C.publish('sensors/', k.encode(), qos=0))  # publish message to mqtt broker
        ]
        yield from asyncio.wait(tasks)
        #logger.info("messages published")  # logger for development
        yield from self.C.disconnect()  # disconnect from mqtt broker
    
    @asyncio.coroutine
    def receive(self):
        yield from self.C.connect('mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io')
        yield from self.C.subscribe([
            ('sensors/', QOS_0),
        ])
        try:
            for i in range(1, 100):
                message = yield from self.C.deliver_message()
                packet = message.publish_packet
                print("%d:  %s => %s" % (i, packet.variable_header.topic_name, str(packet.payload.data)))
            yield from self.C.unsubscribe(['sensors/'])
            yield from self.C.disconnect()

        except ClientException as ce:
            print('kk')

def camStream(ip,port):
    # start a thread that will perform motion detection
	t = threading.Thread(target=cam.detect_motion, args=(64,))
	t.daemon = True
	t.start()

	# start the flask app
	cam.app.run(host=ip, port=port, debug=True,
		threaded=True, use_reloader=False)

