from celery import Celery
from celery.schedules import crontab

cel = Celery('celerytask')
cel.config_from_object('django.conf:settings', namespace='CELERY')
cel.autodiscover_tasks()

if __name__ == '__main__':
    cel.start()

cel.conf.beat_schedule = {
    "scraper-task": {
        "task": "celerytask.tasks.scrap_all",
        "schedule": crontab(minute="*")
    }
}