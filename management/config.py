#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import
from datetime import timedelta

BROKER_URL = 'django://'


# CELERYBEAT_SCHEDULE = {
#     'add-every-2-seconds': {
#          'task': 'management.tasks.add',
#          'schedule': timedelta(seconds=2),
#          'args': (16, 16)
#     },
# }