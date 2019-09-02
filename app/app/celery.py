from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

#Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', broker='amqp://riikuyvl:WtYUU4rdx0-UOTPE0yrObjMZt4WXuAxh@crane.rmq.cloudamqp.com/riikuyvl')
app.conf.task_routes = {
    'decks.tasks.*': {'queue': 'decks'}
}

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def send_user_deck(self, text):
    return text