from celery import Celery

app = Celery("celery-task")
app.config_from_object("celeryconfig")


@app.task
def add_numbers():
    return


app.autodiscover_tasks()
