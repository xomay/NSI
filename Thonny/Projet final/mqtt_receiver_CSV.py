import random
import csv

from paho.mqtt import client as mqtt_client


broker = 'localhost'
port = 1883
topic = "test/win"
# generate client ID with pub prefix randomly

client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'

with open('Data.csv', 'w', newline='') as fichiercsv:
    writer = csv.writer(fichiercsv)
    writer.writerow(['Temperature', 'Temps'])
file = 'Data.csv'
i = 0
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    global file
    def on_message(client, userdata, msg):
        global i
        i+=1
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        print(int(msg.payload.decode()))
        value=msg.payload.decode()
        # create CSV file
        with open(file, 'a', newline='', encoding='utf-8') as fichiercsv:
            writer=csv.writer(fichiercsv)
            writer.writerow([value, i])

    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()

