import paho.mqtt.client as mqtt
import ssl
import json

class MqttCommunicator:
    def __init__(self):
        mqttc = mqtt.Client()
        #mqttc.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED, tls_version=None)
        mqttc.username_pw_set("eecfbf0c", "59ea275059b9c893")
        mqttc.connect("mqtt://eecfbf0c:59ea275059b9c893@broker.shiftr.io")
        

    def send(self):
        msg_txt = {'bpm': 50, 'lidar': [0, 20, 10, 70]}
        txt = json.dumps(msg_txt)
        infot = self.mqttc.publish(topic="humanMap", payload=txt, qos=0, retain=False)
        infot.wait_for_publish()
