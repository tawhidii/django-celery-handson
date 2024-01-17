from celery import Celery

app = Celery("celery-task")
app.config_from_object("celeryconfig")

# import tasks in standalone worker
app.conf.imports = ("newapp.tasks",)


app.autodiscover_tasks()
