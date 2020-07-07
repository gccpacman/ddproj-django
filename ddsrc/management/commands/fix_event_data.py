from io import BytesIO
from datetime import datetime
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddsrc.models import Event


class Command(BaseCommand):
    help = 'Fetching photo data from Library'

    def handle(self, *args, **options):
        events = Event.objects.all()

        for event in events:
            rItem = event.raw
            if rItem.get('begin'):
                try:
                    event.event_begin = datetime.strptime(rItem['begin'], '%Y-%m-%d')
                except ValueError as e:
                    print(rItem['begin'])
            if rItem.get('end'):
                try:
                    event.event_end = datetime.strptime(rItem['end'], '%Y-%m-%d')
                except ValueError as e:
                    print(rItem['end'])
            event.save()
