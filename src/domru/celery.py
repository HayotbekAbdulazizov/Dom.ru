from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab




os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'domru.settings')

app = Celery('domru')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'multiply-task-crontab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (16, 16),
    # },
    'save_contacts': {
        'task': 'save_contacts',
        'schedule': 30.0,
        # 'schedule': crontab(minute="*/3"),

    },

    # 'parse_posts': {
    #     'task': 'parse_posts',
    #     'schedule': 30.0,
    #     # 'schedule': crontab(minute="*/1"),
    # },

    # 'testprint': {
    #     'task': 'testprint',
    #     'schedule': 2.0,

    # },
    # 'testprint2': {
    #     'task': 'testprint2',
    #     'schedule': 3.0,

    # },
    # 'add-every-30-seconds': {
    #     'task': 'movies.tasks.add',
    #     'schedule': 30.0,
    #     'args': (16, 16)
    # },
}

