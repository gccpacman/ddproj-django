import requests
from django.core.management.base import BaseCommand

from ddproj.settings import SHANGHAI_LIBRARY_API_KEY as token
from ddmovie.models import Movie
from time import sleep

def insert_data(rData):
    if rData and len(rData) > 0:
        for rItem in rData:
            mUri = rItem['uri']
            movie, created = Movie.objects.get_or_create(uri=mUri)
            if not created:
                continue
            movie.raw = rItem
            movie.name = rItem['name']
            movie.movie_type = rItem['type']
            movie.pub_date = rItem['date']
            dResponse = requests.get(
                "http://data1.library.sh.cn/shnh/dydata/webapi/movie/movieDetail?uri={}&key={}".format(mUri, token))
            if dResponse.status_code == 200:
                drJson = dResponse.json()
                if drJson['data'] and len(drJson['data']) > 0:
                    movie.detail_raw = drJson['data'][0]
            movie.save()
            print('{} {}'.format(movie.name, movie.uri))
    else:
        print('rData no exist.')


class Command(BaseCommand):
    help = 'Fetching movie data from Library'

    def handle(self, *args, **options):
        page_th = 1
        response = requests.get(
            "http://data1.library.sh.cn/shnh/dydata/webapi/movie/getMovie?pageth={}&key={}".format(page_th, token))
        r_json = response.json()
        insert_data(r_json['data'])
        while r_json['result'] == "0":
            response = requests.get(
            "http://data1.library.sh.cn/shnh/dydata/webapi/movie/getMovie?pageth={}&key={}".format(page_th, token))
            r_json = response.json()
            insert_data(r_json['data'])
            page_th += 1
            sleep(0.5)
