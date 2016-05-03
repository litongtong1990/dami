# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-03 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_humidity_lux_temperature'),
    ]

    operations = [
        migrations.CreateModel(
            name='sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=128)),
                ('sensor_type', models.CharField(max_length=128)),
                ('data', models.FloatField(blank=True, default=None, null=True)),
                ('record_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.DeleteModel(
            name='humidity',
        ),
        migrations.DeleteModel(
            name='lux',
        ),
        migrations.DeleteModel(
            name='temperature',
        ),
    ]