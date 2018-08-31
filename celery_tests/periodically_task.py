
from celery import Celery
from celery.schedules import crontab

app = Celery()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(5, test.s("hello"), expires=10)


@app.task
def test(args):
    print(args)
