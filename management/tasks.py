from celery import task
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt_client
from models import sensor
from django.utils import timezone


def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.


    for sensor in ['temperature','humidity','lux']:
        for i in range(1,7):
            id_name = 'id'+str(i)
            topic = sensor + '/'+ id_name
            client.subscribe(topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    topic = msg.topic
    sensor_type = topic.split('/')[0]
    sensor_id = topic.split('/')[1]
    data = msg.payload
    current_time = timezone.now()
    S = sensor(sensor_type=sensor_type, sensor_id=sensor_id,data=data,record_date=timezone.now())
    S.save()


@task()
def add(x, y):
    return x + y


@task()
def testtest():
    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("10.75.6.80", 1883, 60)
    client.loop_forever()
