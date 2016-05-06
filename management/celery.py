#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from celery import Celery
from django.conf import settings  # noqa
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LM.settings')
app = Celery('management', include=['management.tasks'])
app.config_from_object('management.config')


if __name__ == '__main__':
    app.start()