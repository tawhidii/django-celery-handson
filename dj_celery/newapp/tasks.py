from celery import shared_task


@shared_task
def task1():
    print("I am task1")
    return True


@shared_task
def task2():
    print("I am task2")
    return True
