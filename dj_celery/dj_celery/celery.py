import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_celery.settings")
app = Celery("dj_celery")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.task_routes = {
    "newapp.tasks.task1": {"queue": "queue1"},
    "newapp.tasks.task2": {"queue": "queue2"},
}

app.autodiscover_tasks()