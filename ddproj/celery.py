from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from ddproj.dataset import PeotryTokenizer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ddproj.settings')
app = Celery('ddproj')
app.conf.task_default_queue = 'ddpeotry'
app.config_from_object('django.conf:settings') 
app.autodiscover_tasks()

peotryTokenizer = PeotryTokenizer()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))