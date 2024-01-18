from celery import shared_task


@shared_task
def task1(queue="celery"):
    print("I am task --> 1")
    return True


@shared_task
def task2(queue="celery:1"):
    print("I am task --> 2")
    return True


@shared_task
def task3(queue="celery:2"):
    print("I am task --> 3")
    return True


@shared_task
def task4(queue="celery:3"):
    print("I am task --> 4")
    return True
