import requests
from django.core.management.base import BaseCommand

from ddproj.settings import SHANGHAI_LIBRARY_API_KEY
from ddsrc.models import Event, EventRelation

from io import BytesIO
from django.core.files.base import File
from datetime import datetime
from time import sleep

class Command(BaseCommand):
    help = 'Fetching event data from Library'

    def handle(self, *args, **options):
        events = Event.objects.all()
        relationTypeList = ['person', 'organization', 'opera', 'magazine', 'place', 'movie', 'drama', 'music']
        for event in events:
            response = requests.get(
                "http://data1.library.sh.cn/webapi/hsly/route/getEventDetail?uri={}&key={}".format(event.uri, SHANGHAI_LIBRARY_API_KEY))
            r_json = response.json()
            print(r_json)
            if r_json['data'] and len(r_json['data']) > 0:
                r_data = r_json['data'][0]
                if r_data:
                    print(event.event_title, event.uri)
                    # print(r_data)
                    event.detail_raw = r_data
                    event.description = r_data['description']
                    event.save()
                    for relationType in relationTypeList:
                        relations = r_data.get(relationType+"List")
                        if relations:
                            for relation in relations:
                                event_relation, created = EventRelation.objects.get_or_create(
                                    event_uri=event.uri,
                                    relation_uri=relation.get('uri'),
                                    relation_label=relation.get('label'),
                                    relation_type=relationType
                                )
                                print(event_relation.relation_uri, event_relation.relation_label)
            sleep(0.2)

                