import time
import json
import requests
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from ddsrc.models import Architecture, Road

class Command(BaseCommand):
    help = 'Fetching road data from Library'

    def add_arguments(self, parser):
        parser.add_argument('is_red', nargs='+', type=int)

    def handle(self, *args, **options):
        page_id = 9
        is_red = options['is_red'][0]
        while(self.fetch_page(page_id, is_red)):
            page_id = page_id + 1
            time.sleep(3)

    def fetch_page(self, page_id, is_red):
        url = "http://data1.library.sh.cn/shnh/gmwx/webapi/architecture/getArchitectures"
        querystring = {"isRed": is_red,"key":"3f5df65840c93fea3c1026b8a64649dffa3d6328", "pageSize":"50"}
        querystring['pageth'] = page_id
        response = requests.request('GET', url, params=querystring)
        json_data = response.json()
        if(json_data['result'] != "0"):
            self.stdout.write(self.style.WARNING('Failed import page "%s"' % page_id))
            return False
        hb_data = json_data['data']
        for hb_item in hb_data:
            name_chs=hb_item['nameS']
            if name_chs:
                architecture, created = Architecture.objects.get_or_create(name_chs=name_chs)
                architecture.lib_is_red = is_red
                architecture.name_cht = hb_item['nameT']
                architecture.name_en = hb_item['nameE']
                architecture.lib_uri = hb_item['uri']
                architecture.first_image_lib_uri = hb_item['firstImg']
                if hb_item.get('firstImgPath'):
                    architecture.first_image_uri = hb_item['firstImgPath']
                architecture.protect_type = hb_item['type']
                architecture.address = hb_item['address']
                architecture.house_number = hb_item['houseNumber']
                architecture.road_name_chs = hb_item['road']
                architecture.road_lib_uri = hb_item['roadUri']
                try:
                    road = Road.objects.get(lib_uri=hb_item['roadUri'])
                    architecture.road = road
                except Road.DoesNotExist:
                    pass 
                if hb_item.get('long'):
                    architecture.longitude = hb_item['long']
                if hb_item.get('lat'):
                    architecture.latitude = hb_item['lat']
                architecture.place_uri = hb_item['placeUri']
                architecture.place_name = hb_item['placeValue']
                architecture.des = hb_item['des']
                architecture.lib_update_time = timezone.now()
                architecture.save()
        self.stdout.write(self.style.SUCCESS('Successfully import page "%s"' % page_id))
        return True