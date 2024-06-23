
from django.core.cache import cache
from users.models import RequestLog
from users.models import User
from celery import shared_task
from django.core.mail import send_mail
from main.models import Task
from datetime import datetime

@shared_task(ignore_result = True)
def send_mail_hello(to, body):
    send_mail('Самара детям', body, 'promo@samara.ru', [to])


@shared_task(ignore_result = True)
def send_mail_excursions():
    tasks = Task.objects.all()
    users = User.objects.all()

    if tasks and users:
        send_mail('Самара детям', ', '.join(task.short_task for task in tasks), 'promo@samara.ru', [user.email for user in users])

@shared_task
def save_logs_to_db():
    log_entry = cache.get('request_logs')

    if not log_entry:
        return

    for entry in log_entry:
        user = None

        if isinstance(entry['user_id'], (int, str)):
            user = User.objects.get(id = entry['user_id'])

        RequestLog.objects.create(
            user=user if user else None,
            method=entry['method'],
            path=entry['path'],
            client_ip=entry['client_ip'],
            user_agent=entry['user_agent'],
            timestamp=entry['timestamp'],
        )

    cache.delete('request_logs')
