#!/usr/bin/python
import paho.mqtt.client as mqtt
import time

# Called when connect to Broker
def on_VLCConnect(client, userdata, flags, rc):
    print("Connected with result code {}".format(rc))

# Called when publish
def on_VLCPublish(client, userdata, mid):
    print("OK")

client = mqtt.Client()
client.on_connect = on_VLCConnect
client.on_publish = on_VLCPublish

client.connect("broker.hivemq.com", 1883, 60)

count = 1
while count > 0:
    try:
        id = 1
        message = "Hello, World"
        print("Publish VLCIP/{}/data".format(id))
        client.publish("VLCIP/{}/data".format(id), message)
        time.sleep(3)
        count = count - 1
    except KeyboardInterrupt:
        print("EXIT")
        client.exit()
        sys.exit(0)