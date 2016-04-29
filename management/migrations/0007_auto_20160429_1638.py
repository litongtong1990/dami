# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-29 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_suyuan'),
    ]

    operations = [
        migrations.CreateModel(
            name='controller_db',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('controller_id', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('record_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.AlterField(
            model_name='suyuan',
            name='field2',
            field=models.CharField(max_length=128),
        ),
    ]
