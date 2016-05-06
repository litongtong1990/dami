from __future__ import absolute_import
from management.celery import app

#from celery import task
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt_client
from management.models import sensor,Environment_Daily_new
from django.utils import timezone
import datetime


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




@app.task
def testtest():
    client = mqtt_client.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("10.75.6.80", 1883, 60)
    client.loop_forever()



@app.task
def crontab_daily():

    sensor_all=sensor.objects.all()

    record_date_list=[]
    for item in sensor_all:
        record_date=[item.record_date.year,item.record_date.month,item.record_date.day]
        if record_date not in record_date_list:
            record_date_list.append(record_date)

    sensor_types = sensor.objects.values('sensor_type').distinct()
    sensor_ids = sensor.objects.values('sensor_id').distinct()        
    E_list=[]
    for record_date in record_date_list:
        year=record_date[0]
        month=record_date[1]
        day=record_date[2]      

        for sensor_type in sensor_types:
            for sensor_id in sensor_ids:

                if sensor_type['sensor_type'] == 'temperature':

                    result=sensor_all.filter(record_date__contains=datetime.date(year, month, day),sensor_type__contains=sensor_type['sensor_type'],sensor_id__contains=sensor_id['sensor_id'])                    
                    # Calculate the average value of temperature
                    temperature_list=[item.data for item in result]
                    temperature_average=sum(temperature_list)/len(temperature_list)
                    temperature_low=min(temperature_list)
                    temperature_high=max(temperature_list)
                    E = Environment_Daily_new(sensor_id=sensor_id['sensor_id'],temperature=temperature_average,temperature_low=temperature_low,temperature_high=temperature_high,
                                          record_date=datetime.date(year, month, day))                
                    E_list.append(E)       

                elif sensor_type['sensor_type'] == 'humidity':

                    result=sensor_all.filter(record_date__contains=datetime.date(year, month, day),sensor_type__contains=sensor_type['sensor_type'],sensor_id__contains=sensor_id['sensor_id'])
                    # Calculate the average value humidity
                    humidity_list=[item.data for item in result]
                    humidity_average=sum(humidity_list)/len(humidity_list)
                    humidity_low=min(humidity_list)
                    humidity_high=max(humidity_list)

                    E = Environment_Daily_new(sensor_id=sensor_id['sensor_id'],humidity=humidity_average,humidity_low=humidity_low,humidity_high=humidity_high,
                                          record_date=datetime.date(year, month, day))            
                    E_list.append(E)

                elif sensor_type['sensor_type'] == 'lux':

                    result=sensor_all.filter(record_date__contains=datetime.date(year, month, day),sensor_type__contains=sensor_type['sensor_type'],sensor_id__contains=sensor_id['sensor_id'])
                    # Calculate the average value lux
                    light_list=[item.data for item in result]
                    light_average=sum(light_list)/len(light_list)
                    light_low=min(light_list)
                    light_high=max(light_list)
                    E = Environment_Daily_new(sensor_id=sensor_id['sensor_id'],light=light_average,light_high=light_high,light_low=light_low,
                                          record_date=datetime.date(year, month, day))            
                    E_list.append(E)
                    print "Calculate the history data of %s-%s-%s successfully!"%(str(year),str(month),str(day))

    Environment_Daily_new.objects.bulk_create(E_list)            