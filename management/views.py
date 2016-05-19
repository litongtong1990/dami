from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import MyUser, Book, Img,Environment,Environment_Daily,Environment_Weekly,Environment_Monthly,Suyuan,Environment_Daily_new
from django.core.urlresolvers import reverse, reverse_lazy
from utils import permission_check
import qrcode
from cStringIO import StringIO
from django.http import HttpResponse
import json
from django.utils import timezone
import datetime
import os
import controllers

from django.conf import settings
from django.db.models import Q
#from django.conf.settings import PROJECT_ROOT



#====== this is added for sensor===============
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

#import pycurl
from StringIO import StringIO


import sys
import logging
#import modbus_tk_min.modbus
#import modbus_tk_min.defines as cst
#import modbus_tk_min.modbus_tcp as modbus_tcp
import modbus_tk.modbus
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import time
##################################################

import logging
logger = logging.getLogger(__name__)


def my_scheduled_job():

    server_location = "external"
    server_location = "internal"

    os_env = "linux"
    os_env = "windows"

    total_count = 10000000
    count = 0
    sleep_time = 0.1

    gate_adr = '101.86.93.63'

    gate_port = 502

    sensor_temp_adr = 8
    sensor_temp_adr = 9

    sensor_lux_adr = 1
    sensor_lux_adr = 1

    master = modbus_tcp.TcpMaster(host= gate_adr, port = gate_port)
    master.set_timeout(5.0)

    temperature_humidity = master.execute(sensor_temp_adr, cst.READ_HOLDING_REGISTERS, 0, 2)

    temperature = temperature_humidity[0]
    humidity= temperature_humidity[1]
    lux = master.execute(sensor_lux_adr, cst.READ_HOLDING_REGISTERS, 0, 1)[0]

    # content = {
    #     'temperature': temperature,
    #     'humidity': humidity,
    #     'lux':lux
    # }


    E = Environment(temperature=temperature, humidity=humidity,light=lux,record_date=timezone.now())
    E.save()
    print "save the sensor data to database successfully!"





def crontab_daily(request):

    #Environment.objects.filter(record_date=timezone.now())
    environment_all=Environment.objects.all()
    record_date_list=[]
    for item in environment_all:
        record_date=[item.record_date.year,item.record_date.month,item.record_date.day]
        if record_date not in record_date_list:
            record_date_list.append(record_date)
    
    for record_date in record_date_list:
        year=record_date[0]
        month=record_date[1]
        day=record_date[2]
        print year,month,day        

        result=Environment.objects.filter(record_date__contains=datetime.date(year, month, day))
        # Calculate the average value of temperature,humidity and light
        temperature_list=[item.temperature for item in result]
        temperature_average=sum(temperature_list)/len(temperature_list)
        temperature_low=min(temperature_list)
        temperature_high=max(temperature_list)

        
        humidity_list=[item.humidity for item in result]
        humidity_average=sum(humidity_list)/len(humidity_list)
        humidity_low=min(humidity_list)
        humidity_high=max(humidity_list)

        light_list=[item.light for item in result]
        light_average=sum(light_list)/len(light_list)
        light_low=min(light_list)
        light_high=max(light_list)


        E = Environment_Daily(temperature=temperature_average,temperature_low=temperature_low,temperature_high=temperature_high,
                              humidity=humidity_average,humidity_low=humidity_low,humidity_high=humidity_high,
                              light=light_average,light_high=light_high,light_low=light_low,
                              record_date=datetime.date(year, month, day))
        E.save()
        print "Calculate the history data of %s-%s-%s successfully!"%(str(year),str(month),str(day))


    #print timezone.now()

    return HttpResponse("Get the data successfully")    






def crontab_daily_incremental():

    
    year=timezone.now().year
    month=timezone.now().month
    day=timezone.now().day

    result=Environment.objects.filter(record_date__contains=datetime.date(year, month, day))
    # Calculate the average value of temperature,humidity and light
    temperature_list=[item.temperature for item in result]
    temperature_average=sum(temperature_list)/len(temperature_list)
    
    humidity_list=[item.humidity for item in result]
    humidity_average=sum(humidity_list)/len(humidity_list)

    light_list=[item.light for item in result]
    light_average=sum(light_list)/len(light_list)

    E = Environment_Daily(temperature=temperature_average, humidity=humidity_average,light=light_average,record_date=datetime.date(year, month, day))
    E.save()
    

    print "Calculate the history data of %s-%s-%s successfully!"%(str(year),str(month),str(day))

    #return HttpResponse("Calculate the last date successfully")  





def index_test(request):


    state = None

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index_test'))
        else:
            state = 'not_exist_or_password_error'

            content = {
                'active_menu': 'homepage',
                'state': state,
                'user': None
            }

            return render(request, 'management/login.html', content)

    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'management/index_test.html', content)



def fields(request,field_name):

    user = request.user if request.user.is_authenticated() else None
    
    content = {
        'active_menu': 'homepage',
        'user': user,
        'field_name':field_name
    }

    return render(request, 'management/qrcode_suyuan.html', content)



def suyuan(request):
    user = request.user if request.user.is_authenticated() else None
    content = {
        'active_menu': 'homepage',
        'user': user,
    }
    return render(request, 'management/suyuan.html', content)



# this is for add the temperature_humidity and lux
def json_test(request):

    server_location = "external"
    server_location = "internal"

    os_env = "linux"
    os_env = "windows"

    total_count = 10000000
    count = 0
    sleep_time = 0.1

    gate_adr = '101.86.93.63'

    gate_port = 502

    sensor_temp_adr = 8
    # sensor_temp_adr = 9

    sensor_lux_adr = 1
    sensor_lux_adr = 1

    master = modbus_tcp.TcpMaster(host= gate_adr, port = gate_port)
    master.set_timeout(5.0)

    temperature_humidity = master.execute(sensor_temp_adr, cst.READ_HOLDING_REGISTERS, 0, 2)

    temperature = temperature_humidity[0]
    humidity= temperature_humidity[1]
    lux = master.execute(sensor_lux_adr, cst.READ_HOLDING_REGISTERS, 0, 1)[0]

    content = {
        'temperature': temperature,
        'humidity': humidity,
        'lux':lux
    }


    # E = Environment(temperature=temperature, humidity=humidity,light=lux,record_date=timezone.now())
    # E.save()

    jsondata = json.dumps(content) 
    return HttpResponse(jsondata)




def signup(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index_test'))
    state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':
            state = 'empty'
        elif password != repeat_password:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = MyUser(user=new_user, nickname=request.POST.get('nickname', ''))
                new_my_user.save()
                state = 'success'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None,
    }
    return render(request, 'management/signup.html', content)


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('index_test'))
    state = None
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index_test'))
        else:
            state = 'not_exist_or_password_error'
    content = {
        'active_menu': 'homepage',
        'state': state,
        'user': None
    }
    return render(request, 'management/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index_test'))


@login_required(login_url=reverse_lazy('login'))
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'management/set_password.html', content)


# @user_passes_test(permission_check, login_url=reverse_lazy('login'))





@login_required(login_url=reverse_lazy('login'))

def add_book(request):
    user = request.user
    state = None
    if request.method == 'POST':
        

        new_suyuan = Suyuan(
                field1=request.POST.get('field1', ''),
                field2=request.POST.get('field2', ''),
                field3=request.POST.get('field3', ''),
                field4=request.POST.get('field4', '')
                
        )
        
        new_suyuan.save()

        state = 'success'
    content = {
        'user': user,
        'active_menu': 'add_book',
        'state': state,
    }
    return render(request, 'management/add_book.html', content)



def control(request):
    user = request.user if request.user.is_authenticated() else None
    state = None
    if request.method == 'POST':
        
        state=request.POST.get('state','')
        controller_id=request.POST.get('controller_id','')

        if state == 'true':
            #result = control_light('open')
            result = controllers.light_control(controller_id,'open')
            #print result
            print "the light is on...."
            logger.info("the light is on....")
        else:
            #result = control_light('close')
            result = controllers.light_control(controller_id,'close')
            #print result
            print "the light if off...."
            logger.info("the light is off....")
        state = 'success'


    path = os.path.join(settings.PROJECT_ROOT, 'controller_config.json')
    display = controllers.get_string_from_json(path)
    content = {
        'user': user,
        'active_menu': 'add_book',
        'state': state,
        'display':display
    }
    return render(request, 'management/control.html', content)





def mqtt(request):
    user = request.user if request.user.is_authenticated() else None
    state = None    
    path = os.path.join(settings.PROJECT_ROOT, 'sensor_config.json')
    display = controllers.get_string_from_json(path)
    

    #latest_data=Environment_Daily.objects.order_by('-record_date')[0:4]

    total_data = Environment_Daily_new.objects
    total_number = len(total_data.all())
    id_number = total_data.order_by('sensor_id').values('sensor_id').distinct()
    temperature_data = total_data.order_by('-record_date').filter(~Q(temperature = None))[0:max(len(id_number)*4,total_number)]
    humidity_data = total_data.order_by('-record_date').filter(~Q(humidity = None))[0:max(len(id_number)*4,total_number)]
    light_data = total_data.order_by('-record_date').filter(~Q(light = None))[0:max(len(id_number)*4,total_number)]


    content = {
        'user': user,
        'active_menu': 'add_book',
        'state': state,
        'display':display,
        'temperature_data':temperature_data,
        'humidity_data':humidity_data,
        'light_data':light_data
    }
       
    return render(request, 'management/mqtt.html', content)




def control_light(status):
    gate_adr = '192.168.0.201'
    gate_adr = '192.168.0.200'
    gate_adr = '101.86.93.63'
    gate_port = 502

    count = 0
    sleep_time = 0.1

    control_adr = 16

    control_channel = 0
    control_channel = 1


    #Connect to the slave
    #master = modbus_tcp.TcpMaster(host='192.168.0.7', port=502)
    master = modbus_tcp.TcpMaster(host= gate_adr, port = gate_port)
    master.set_timeout(5.0)

    #this is the api to control the relay
    #control_channel, there are totally two relays, 0 and 1
    #the last parameter is the status of the relay, 0 means open, 1 means close
    
    if status=='close':
        master.execute(control_adr, cst.WRITE_SINGLE_COIL, control_channel, 1, 1)     #close channel 1
          
    else:
        master.execute(control_adr, cst.WRITE_SINGLE_COIL, control_channel, 1, 0)     #open channel 1

    control_status = master.execute(control_adr, cst.READ_COILS, control_channel, 1 ) 
    time.sleep(sleep_time)
    return control_status[0]



def view_book_list(request):
    user = request.user if request.user.is_authenticated() else None
    category_list = Book.objects.values_list('category', flat=True).distinct()
    query_category = request.GET.get('category', 'all')
    if (not query_category) or Book.objects.filter(category=query_category).count() is 0:
        query_category = 'all'
        book_list = Book.objects.all()
    else:
        book_list = Book.objects.filter(category=query_category)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        book_list = Book.objects.filter(name__contains=keyword)
        query_category = 'all'

    paginator = Paginator(book_list, 5)
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'view_book',
        'category_list': category_list,
        'query_category': query_category,
        'book_list': book_list,
    }
    return render(request, 'management/view_book_list.html', content)





def video(request):
    user = request.user if request.user.is_authenticated() else None
    category_list = Book.objects.values_list('category', flat=True).distinct()
    query_category = request.GET.get('category', 'all')
    if (not query_category) or Book.objects.filter(category=query_category).count() is 0:
        query_category = 'all'
        book_list = Book.objects.all()
    else:
        book_list = Book.objects.filter(category=query_category)

    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        book_list = Book.objects.filter(name__contains=keyword)
        query_category = 'all'

    paginator = Paginator(book_list, 5)
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    content = {
        'user': user,
        'active_menu': 'realtime_video',
        'category_list': category_list,
        'query_category': query_category,
        'book_list': book_list,
    }
    return render(request, 'management/video.html', content)




# This function is to for generate the qrcode for a specific URL
def qrcode_generate_page(request, field_name):
    url="http://127.0.0.1:8000/fields/"+field_name
    print "====="
    print url
    print "====="
    img = qrcode.make(url)
    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response



def detail(request):
    user = request.user if request.user.is_authenticated() else None
    book_id = request.GET.get('id', '')
    if book_id == '':
        return HttpResponseRedirect(reverse('view_book_list'))
    try:
        book = Book.objects.get(pk=book_id)
    except:
        return HttpResponseRedirect(reverse('view_book_list'))
    content = {
        'user': user,
        'active_menu': 'view_book',
        'book': book,
    }
    return render(request, 'management/detail.html', content)



#@user_passes_test(permission_check, login_url=reverse_lazy('login'))
@login_required(login_url=reverse_lazy('login'))
def generate_qrcode(request):
    user = request.user
    state = None
    name = None

    if request.method == 'POST':
        try:
            name=request.POST.get('name', '')
            # new_img = Img(
            #         name=request.POST.get('name', ''),
            #         description=request.POST.get('description', ''),
            #         img=request.FILES.get('img', ''),
            #         book=Book.objects.get(pk=request.POST.get('book', ''))
            # )
            # new_img.save()
        
        except Exception, e:
            state = 'error'
            print e
        else:
            state = 'success'
    content = {
        'user': user,
        'state': state,
        'book_list': Book.objects.all(),
        'active_menu': 'add_img',
        'name':name,
    }
    return render(request, 'management/generate_qrcode.html', content)


def realtime_info(request):
    user = request.user if request.user.is_authenticated() else None
    state = None
    name = None

    latest_data=Environment_Daily.objects.order_by('-record_date')[0:4]


    if request.method == 'POST':
        try:
            name=request.POST.get('name', '')
            # new_img = Img(
            #         name=request.POST.get('name', ''),
            #         description=request.POST.get('description', ''),
            #         img=request.FILES.get('img', ''),
            #         book=Book.objects.get(pk=request.POST.get('book', ''))
            # )
            # new_img.save()
        
        except Exception, e:
            state = 'error'
            print e
        else:
            state = 'success'


    content = {
        'user': user,
        'state': state,
        'book_list': Book.objects.all(),
        'active_menu': 'realtime_info',
        'name':name,
        'latest_data':latest_data
    }
    return render(request, 'management/realtime_info.html', content)








