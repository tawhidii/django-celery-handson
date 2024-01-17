from celery import shared_task


@shared_task
def task2():
    print("I am task2")
    return True
