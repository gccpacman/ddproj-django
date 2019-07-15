import time
import json
import requests
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from ddsrc.models import Road

class Command(BaseCommand):
    help = 'Fetching road data from Library'

    # def add_arguments(self, parser):
    #     parser.add_argument('page_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        page_id = 1
        while(self.fetch_page(page_id)):
            page_id = page_id + 1
            time.sleep(3)

    def fetch_page(self, page_id):
        url = "http://data1.library.sh.cn/shnh/wkl/webapi/road/list"
        querystring = {"type":"2","key":"3f5df65840c93fea3c1026b8a64649dffa3d6328", "pageSize":"50"}
        querystring['pageth'] = page_id
        response = requests.request('GET', url, params=querystring)
        json_data = response.json()
        if(json_data['result'] != "0"):
            self.stdout.write(self.style.WARNING('Failed import page "%s"' % page_id))
            return False
        hb_data = json_data['data']
        for hb_item in hb_data:
            name_chs=hb_item['nameChs']
            if name_chs:
                road, created = Road.objects.get_or_create(name_chs=name_chs)
                road.name_en = hb_item['nameEn']
                road.lib_uri = hb_item['uri']
                road.temporal_value = hb_item['temporalValue']
                road.history_of_name = hb_item['historyOfName']
                road.name_after = hb_item['nameAfter']
                place_list = hb_item['placeList']
                if place_list and len(place_list) > 0:
                    road.place_uri = place_list[0]['placeUri']
                    road.place_name = place_list[0]['placeName']
                road.lib_update_time = timezone.now()
                road.save()
        self.stdout.write(self.style.SUCCESS('Successfully import page "%s"' % page_id))
        return True