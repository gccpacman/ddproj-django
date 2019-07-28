import time
import json
import requests
from random import randrange
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from ddproj.settings import GAODE_MAP_WEBAPI_KEY
from ddsrc.models import Road
from ddsrc.tools import gcj02_to_bd09

class Command(BaseCommand):
    help = 'Fetching road polylines from Gaode API'

    def handle(self, *args, **options):
        self.fetch_page()

    def gcj02_to_bd09_str(self, point):
        lng, lat = point.split(",")
        lng_bd, lat_bd = gcj02_to_bd09(float(lng), float(lat))
        return {"lng": str(lng_bd), "lat": str(lat_bd)}

    def fetch_page(self):
        for road in Road.objects.all():
            url = "http://restapi.amap.com/v3/road/roadname"
            querystring = {"city":"上海", "key":GAODE_MAP_WEBAPI_KEY, "keywords":road.name_chs}
            response = requests.request('GET', url, params=querystring)
            json_data = response.json()
            roads_list = json_data['roads']
            if len(roads_list) > 0:
                road_gaode = roads_list[0]
                road_gaode_center = road_gaode['center']
                road_gaode_polylines = road_gaode['polylines']
                road_bmap_polylines = [([self.gcj02_to_bd09_str(point) for point in polyline.split(";")]) for polyline in road_gaode_polylines]
                road.polylines_gaode = road_gaode_polylines
                road.center_gaode = road_gaode_center
                road.polylines_bmap = road_bmap_polylines
                road.center_bmap = self.gcj02_to_bd09_str(road_gaode_center)
                road.save()
            self.stdout.write(self.style.SUCCESS('Successfully get gaode polyline "%s"' % road.name_chs))
            sleep_time = randrange(1, 4)
            self.stdout.write(self.style.SUCCESS('sleep "%s" seconds' % sleep_time))
            time.sleep(sleep_time)