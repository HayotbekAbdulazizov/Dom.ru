import os
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta
import main


os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'domru.settings')

app = Celery('domru')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()



# заносим таски в очередь
app.conf.beat_schedule = {
    'every': { 
        'task': 'main.tasks.repeat_order_make',
        # "schedule": crontab(hour=1, minute=6) ,
        "schedule": crontab(minute="*/2"),
        # "options":{
            
        # }
    },         

    'contacts': { 
        'task': 'main.tasks.contacts',
        "schedule": crontab( minute="*") ,
        # "options":{
            # 
        # }
    },                                                           

}