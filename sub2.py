# subscriber
import paho.mqtt.client as mqtt
import json


client = mqtt.Client()
client.connect('192.168.0.106', 1883)

def on_connect(client, userdata, flags, rc):
    print("Connected to a broker!")
    client.subscribe("/IOT")

def on_message(client, userdata, message):
    print(message.payload.decode())
     # Receive data and decode it
    print("topic:", message.topic)
    print("Message received: " + message.payload.decode('utf-8'))
    data = json.loads(message.payload.decode('utf-8'))
    print(data)


    if message.topic == "/IOT":
        print("inside IOT topic" , data)
                
        print(data)
        name = data['name']
        roll = data['roll']
        if name == "xxxx" and roll == xx:
            with open("/home/pi/data.csv", "a+") as file:
                file.write(str(name)+','+str(roll))
                file.write("\n")




while True:
    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_forever()
