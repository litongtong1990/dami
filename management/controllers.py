import json
import paho.mqtt.publish as publish
from models import controller_db
from django.utils import timezone

def get_string_from_json(path):
    
    file_object = open(path)
    json_string = file_object.read()
    json_file= json.loads(json_string)
    return json_file


def light_control(light_control,status):
    
    topic = light_control + '/' + 'status'
    msgs = [
        {'topic':topic, 'payload':status}
        ]    
    print msgs
    publish.multiple(msgs, hostname="10.75.6.80")
    C = controller_db(controller_id=light_control, status=status,record_date=timezone.now())
    C.save()
    return status