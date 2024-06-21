from django.core.management.base import BaseCommand
from main.models import Master

class Command(BaseCommand):
    help = 'Show all masters'

    def handle(self, *args, **options):
        masters = Master.objects.all()
        for master in masters:
            self.stdout.write(f'Master title: {master.title}, Master time_create: {master.time_create}')