#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'django://'


CELERYBEAT_SCHEDULE = {
    'calculate-every-midnight': {
         'task': 'management.tasks.environment_daily_calculation',
         'schedule': crontab(minute=0, hour=0),
         'args': ()
    }

}


