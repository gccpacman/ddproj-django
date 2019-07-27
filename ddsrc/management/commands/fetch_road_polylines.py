import time
import json
import requests
from django.utils import timezone
from django.core.management.base import BaseCommand, CommandError

from ddproj.settings import GAODE_MAP_WEBAPI_KEY
from ddsrc.models import Road
from ddsrc.tools import gcj02_to_bd09

class Command(BaseCommand):
    help = 'Fetching road polylines from Gaode API'

    def handle(self, *args, **options):
        page_id = 1
        while(self.fetch_page(page_id)):
            page_id = page_id + 1
            time.sleep(3)

    def gcj02_to_bd09_str(self, point):
        lng, lat = point.split(",")
        lng_bd, lat_bd = gcj02_to_bd09(float(lng), float(lat))
        return {"lng": str(lng_bd), "lat": str(lat_bd)}

    def fetch_page(self, page_id):
        road_name_chs = "龙茗路"
        url = "http://restapi.amap.com/v3/road/roadname"
        querystring = {"city":"上海","key":GAODE_MAP_WEBAPI_KEY, "keywords":road_name_chs}
        response = requests.request('GET', url, params=querystring)
        json_data = response.json()
        roads_list = json_data['roads']
        if len(roads_list) > 0:
            road_gaode = roads_list[0]
            road_gaode_center = road_gaode['center']
            road_gaode_polylines = road_gaode['polylines']
            road_bmap_polylines = [([self.gcj02_to_bd09_str(point) for point in polyline.split(";")]) for polyline in road_gaode_polylines]
            road = Road.objects.get(name_chs=road_name_chs)
            road.polylines_gaode = road_gaode_polylines
            road.polylines_bmap = road_bmap_polylines
            road.save()
