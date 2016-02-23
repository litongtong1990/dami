# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20160129_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment_Daily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(blank=True, default=None, null=True)),
                ('humidity', models.FloatField(blank=True, default=None, null=True)),
                ('light', models.FloatField(blank=True, default=None, null=True)),
                ('record_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Environment_Monthly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(blank=True, default=None, null=True)),
                ('humidity', models.FloatField(blank=True, default=None, null=True)),
                ('light', models.FloatField(blank=True, default=None, null=True)),
                ('record_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Environment_Weekly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(blank=True, default=None, null=True)),
                ('humidity', models.FloatField(blank=True, default=None, null=True)),
                ('light', models.FloatField(blank=True, default=None, null=True)),
                ('record_date', models.DateTimeField(default=None)),
            ],
        ),
    ]
