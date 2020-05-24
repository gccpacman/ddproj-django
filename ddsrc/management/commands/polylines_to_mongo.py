from django.core.management.base import BaseCommand, CommandError
import simplejson as json
from pymongo import MongoClient
from ddsrc.models import Road


class Command(BaseCommand):

    def handle(self, *args, **options):
        client = MongoClient()
        dd_db = client.ddmongo
        for road in Road.objects.all():
            insert_id = dd_db.roads.insert_one({
                '_id': road._id, 
                'center_bmap': json.loads(road.center_bmap),
                'polylines_bmap':  json.loads(road.polylines_bmap),
                'center_gaode': json.loads(road.center_gaode),
                'polylines_gaode':  json.loads(road.polylines_gaode),
            }).inserted_id
            print('%s %s inserted' % (road._id, insert_id))
