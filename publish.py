import paho.mqtt.publish as publish
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




msgs = []

for sensor in ['temperature','humidity','lux']:
	for i in range(1,7):
		id_name = 'id'+str(i)
		topic = sensor + '/'+ id_name
		item = {'topic':topic,'payload':random.randint(1, 10000)}
		msgs.append(item)


# msgs = [
#     {'topic':"temperature", 'payload':temperature},
#     {'topic':"humidity", 'payload':humidity},
#     {'topic':"lux", 'payload':lux},
#     ]

print msgs


publish.multiple(msgs, hostname="101.86.93.63")



