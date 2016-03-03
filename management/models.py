from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class MyUser(models.Model):
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=16)
    permission = models.IntegerField(default=1)

    def __unicode__(self):
        return self.user.username


class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    author = models.CharField(max_length=128)
    publish_date = models.DateField()
    category = models.CharField(max_length=128)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name


class Img(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    img = models.ImageField(upload_to='image/%Y/%m/%d/')
    book = models.ForeignKey(Book)

    class META:
        ordering = ['name']

    def __unicode__(self):
        return self.name




class Environment(models.Model):
    temperature=models.FloatField(null=True, blank=True, default=None)
    humidity=models.FloatField(null=True, blank=True, default=None)
    # wind_speed=models.FloatField(null=True, blank=True, default=None)
    # wind_direction=models.FloatField(null=True, blank=True, default=None)
    light=models.FloatField(null=True, blank=True, default=None)
    # soid_temperature=models.FloatField(null=True, blank=True, default=None)
    # soid_humidity=models.FloatField(null=True, blank=True, default=None)
    # product_name = models.CharField(max_length=200,default=None)
    record_date = models.DateTimeField(default=None)


class Environment_Daily(models.Model):
    
    temperature=models.FloatField(null=True, blank=True, default=None)
    temperature_low=models.FloatField(null=True, blank=True, default=None)    
    temperature_high=models.FloatField(null=True, blank=True, default=None)    
    humidity=models.FloatField(null=True, blank=True, default=None)
    humidity_low=models.FloatField(null=True, blank=True, default=None)
    humidity_high=models.FloatField(null=True, blank=True, default=None)
    light=models.FloatField(null=True, blank=True, default=None)
    light_low=models.FloatField(null=True, blank=True, default=None)
    light_high=models.FloatField(null=True, blank=True, default=None)        
    record_date = models.DateTimeField(default=None)



class Environment_Weekly(models.Model):
    temperature=models.FloatField(null=True, blank=True, default=None)
    humidity=models.FloatField(null=True, blank=True, default=None)
    # wind_speed=models.FloatField(null=True, blank=True, default=None)
    # wind_direction=models.FloatField(null=True, blank=True, default=None)
    light=models.FloatField(null=True, blank=True, default=None)
    # soid_temperature=models.FloatField(null=True, blank=True, default=None)
    # soid_humidity=models.FloatField(null=True, blank=True, default=None)
    # product_name = models.CharField(max_length=200,default=None)
    record_date = models.DateTimeField(default=None)


class Environment_Monthly(models.Model):
    temperature=models.FloatField(null=True, blank=True, default=None)
    humidity=models.FloatField(null=True, blank=True, default=None)
    # wind_speed=models.FloatField(null=True, blank=True, default=None)
    # wind_direction=models.FloatField(null=True, blank=True, default=None)
    light=models.FloatField(null=True, blank=True, default=None)
    # soid_temperature=models.FloatField(null=True, blank=True, default=None)
    # soid_humidity=models.FloatField(null=True, blank=True, default=None)
    # product_name = models.CharField(max_length=200,default=None)
    record_date = models.DateTimeField(default=None)



