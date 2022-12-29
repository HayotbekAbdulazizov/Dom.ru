import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'domru.settings')

app = Celery('domru')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()



# заносим таски в очередь
app.conf.beat_schedule = {
    'every': { 
        'task': 'main.tasks.repeat_order_make',
        "schedule": timedelta(seconds=2) ,
        "options":{
            
        }
    },                                                           

}