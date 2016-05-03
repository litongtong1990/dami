import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt_client
import random

# try:
#     # python 3
#     from urllib.parse import urlencode
# except ImportError:
#     # python 2
#     from urllib import urlencode

# #import pycurl
# from StringIO import StringIO


# import sys
# import logging
# #import modbus_tk_min.modbus
# #import modbus_tk_min.defines as cst
# #import modbus_tk_min.modbus_tcp as modbus_tcp
# import modbus_tk.modbus
# import modbus_tk.defines as cst
# import modbus_tk.modbus_tcp as modbus_tcp
# import time
# import paho.mqtt.publish as publish

# server_location = "external"
# server_location = "internal"

# os_env = "linux"
# os_env = "windows"

# total_count = 10000000
# count = 0
# sleep_time = 0.1

# gate_adr = '101.86.93.63'

# gate_port = 502

# sensor_temp_adr = 8

# sensor_lux_adr = 1
# sensor_lux_adr = 1

# master = modbus_tcp.TcpMaster(host= gate_adr, port = gate_port)
# master.set_timeout(5.0)

# temperature_humidity = master.execute(sensor_temp_adr, cst.READ_HOLDING_REGISTERS, 0, 2)

# temperature = temperature_humidity[0]
# humidity= temperature_humidity[1]
# lux = master.execute(sensor_lux_adr, cst.READ_HOLDING_REGISTERS, 0, 1)[0]


# # msgs = [
# #     {'topic':"Liyicheng_test", 'payload':"multiple 1"},
# #     ("paho/test/multiple", "multiple 2", 0, False)
# #     ]




# temperature = random.randint(1, 10000)
# humidity = random.randint(1, 10000)
# lux = random.randint(1, 10000)




def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("temperature/id2")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt_client.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.75.6.80", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

client.loop_forever()
#client.loop_start()



