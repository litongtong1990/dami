# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-29 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20160112_2031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(blank=True, default=None, null=True)),
                ('humidity', models.FloatField(blank=True, default=None, null=True)),
                ('light', models.FloatField(blank=True, default=None, null=True)),
                ('record_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='img',
            name='img',
            field=models.ImageField(upload_to='image/%Y/%m/%d/'),
        ),
    ]