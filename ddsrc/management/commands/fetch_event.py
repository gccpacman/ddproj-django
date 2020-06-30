import requests
from django.core.management.base import BaseCommand

from ddproj.settings import SHANGHAI_LIBRARY_API_KEY
from ddsrc.models import Event

from io import BytesIO
from django.core.files.base import File
from datetime import datetime


def insert_data(rData):
    if rData and len(rData) > 0:
        for rItem in rData:
            uri = rItem['uri']
            event, created = Event.objects.get_or_create(uri=uri)
            if not created:
                continue
            event.raw = rItem
            event.event_title = rItem['title']
            if rItem.get('imageList') and len(rItem['imageList']) > 0 and rItem['imageList'][0].get('eventImagePath'):
                img_path = rItem['imageList'][0]['eventImagePath']
                p_response = requests.get(img_path, stream=True, verify=False)
                if p_response.status_code == requests.codes.ok:
                    file_name = img_path.split('/')[-1]
                    fp = BytesIO()
                    fp.write(p_response.content)
                    event.event_image.save(file_name, File(fp))
            event.event_begin = datetime.strptime(rItem['begin'], '%Y-%m-%d')
            event.event_begin = datetime.strptime(rItem['end'], '%Y-%m-%d')
            event.save()
            print('{} {}'.format(event.event_title, event.uri))
    else:
        print('rData no exist.')


class Command(BaseCommand):
    help = 'Fetching event data from Library'

    def handle(self, *args, **options):
        page_th = 1
        response = requests.get(
            "http://data1.library.sh.cn/webapi/hsly/route/getEventList?pageth={}&key={}".format(page_th, SHANGHAI_LIBRARY_API_KEY))
        r_json = response.json()
        insert_data(r_json['data'])
        page_th += 1
        # while r_json['result'] == "0":
        #     response = requests.get(
        #         "http://data1.library.sh.cn/webapi/hsly/route/getEventList?pageth={}&key={}".format(page_th, SHANGHAI_LIBRARY_API_KEY))
        #     r_json = response.json()
        #     insert_data(r_json['data'])
        #     page_th += 1
