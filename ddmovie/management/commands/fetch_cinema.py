import requests
from django.core.management.base import BaseCommand

from ddproj.settings import SHANGHAI_LIBRARY_API_KEY as token
from ddmovie.models import MovieCinema

def insert_data(rData):
    if rData and len(rData) > 0:
        for rItem in rData:
            mUri = rItem['uri']
            cinema, created = MovieCinema.objects.get_or_create(uri=mUri)
            if not created:
                print('{} {} already existed.'.format(cinema.name, cinema.uri))
                continue
            cinema.raw = rItem
            cinema.name = rItem['nameS']
            cinema.nameEn = rItem['nameE']
            cinema.des = rItem['des']
            cinema.architectureUri = rItem['bUri']        
            cinema.save()
            print('{} {}'.format(cinema.name, cinema.uri))
    else:
        print('rData no exist.')


class Command(BaseCommand):
    help = 'Fetching movie data from Library'

    def handle(self, *args, **options):
        page_th = 1
        response = requests.get(
            "http://data1.library.sh.cn/shnh/dydata/webapi/architecture/getArchitecture?pageth={}&key={}".format(page_th, token))
        r_json = response.json()
        insert_data(r_json['data'])
        while r_json['result'] == "0":
            page_th += 1
            response = requests.get(
            "http://data1.library.sh.cn/shnh/dydata/webapi/architecture/getArchitecture?pageth={}&key={}".format(page_th, token))
            if r_json['result'] == "0":
                r_json = response.json()
                insert_data(r_json['data'])
