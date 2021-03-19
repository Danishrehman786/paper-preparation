# publisher
import paho.mqtt.client as mqtt
import json
import time

client = mqtt.Client()
client.connect('192.168.0.106', 1883)

data = {'name' : 'XXXX',
       'roll'  : '25',
       }
data1=json.dumps(data)

while True:
##    client.publish("LINTANGtopic/test", input('Message : '))
    
    client.publish("/IOT", data1)

    time.sleep(5)
