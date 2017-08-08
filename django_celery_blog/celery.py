import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_blog.settings')

app = Celery('django_celery_blog')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'publish.tasks.send_view_count_report',
        'schedule': crontab(),
        # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    }
}
