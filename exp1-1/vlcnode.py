#!/usr/bin/python
import paho.mqtt.client as mqtt
import time

# Called when connect to Broker
def on_VLCConnect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))

# Called when publish
def on_VLCPublish(client, userdata, mid):
    print("Publish OK")

client = mqtt.Client()
client.on_connect = on_VLCConnect
client.on_publish = on_VLCPublish

client.connect("iot.eclipse.org", 1883, 60)

while True:
    try:
        id = 1
        client.publish("VLCIP/" + str(id) + "/data", id)
        time.sleep(3)
    except KeyboardInterrupt:
        print("EXIT")
        client.exit()
        sys.exit(0)
