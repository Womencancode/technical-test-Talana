from celery import shared_task


@shared_task
def hello_task():
    print('Hi! I\'m beat scheduled task provided by celery!')
