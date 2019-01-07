#!/usr/bin/python
import paho.mqtt.client as mqtt

def on_BrokerConnect(client, userdata, flags, rc):
    print("Connected with result code " +str(rc))
    client.subscribe("VLCIP/+/data")
    
def on_BrokerMessage(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_BrokerConnect
client.on_message = on_BrokerMessage

client.connect("iot.eclipse.org", 1883, 60)
client.loop_forever()
