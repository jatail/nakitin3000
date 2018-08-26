from django.core.management.base import BaseCommand, CommandError
from nakit.models import Organization, Event, Nakki, Nakittautuminen, Orgadmin
from datetime import datetime, timedelta


class Command(BaseCommand):
    help = 'Deletes events older than 60 days'
    def handle(self, *args, **options):
        time_threshold = datetime.now() - timedelta(days=30)
        results = Event.objects.filter(date__lt=time_threshold)
        if results.count() != 0:
            print('Nakittimen vanhojen tapahtumien poistoskripti', datetime.now())
            for i in results:
                print(i.name, i.organizer, i.date)
                i.delete()

