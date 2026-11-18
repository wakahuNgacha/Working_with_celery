import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'working_with_celery.settings')
app = Celery("working_with_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


#creating a celery task
@app.task
def add_number():
    return

#to discover other tasks through out the project

