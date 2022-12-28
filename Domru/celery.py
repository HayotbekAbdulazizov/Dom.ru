
import os
from celery import Celery
# from decouple import config
from celery.schedules import crontab
from datetime import timedelta



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Domru.settings')

app = Celery('Domru')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Below is for illustration purposes. We 
# configured so we can adjust scheduling 
# in the Django admin to manage all 
# Periodic Tasks like below
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'multiply-task-crontab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (16, 16),
    # },
    'multiply-every-5-seconds': {
        'task': 'sum_list_numbers',
        # 'schedule': 2.0,
        "schedule": timedelta(seconds=2),
        # 'args': (16, 16)
    },
    # 'add-every-30-seconds': {
    #     'task': 'movies.tasks.add',
    #     'schedule': 30.0,
    #     'args': (16, 16)
    # },
}