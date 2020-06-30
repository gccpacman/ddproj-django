from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddproj.settings import SHANGHAI_LIBRARY_API_KEY as token
from ddmovie.models import MoviePhoto
from time import sleep

def insert_data(rData):
    if rData and len(rData) > 0:
        for rItem in rData:
            mUri = rItem['uri']
            moviePhoto, created = MoviePhoto.objects.get_or_create(uri=mUri)
            if not created:
                continue
            moviePhoto.raw = rItem
            moviePhoto.uri = rItem['uri']
            moviePhoto.photoType = rItem['type']
            moviePhoto.movieUri = rItem['movie']
            if rItem.get('imgPath'):
                imgPath = rItem['imgPath']
                pResponse = requests.get(rItem['imgPath'], stream=True, verify=False)
                print(imgPath)
                if pResponse.status_code == requests.codes.ok:
                    file_name = imgPath.split('/')[-1]
                    fp = BytesIO()
                    fp.write(pResponse.content)
                    moviePhoto.image.save(file_name, File(fp))
            moviePhoto.save()
            print('{} {}'.format(moviePhoto.photoType, moviePhoto.uri))
    else:
        print('rData no exist.')



class Command(BaseCommand):
    help = 'Fetching photo data from Library'

    def handle(self, *args, **options):
        path_th = 1
        response = requests.get(
            "http://data1.library.sh.cn/shnh/dydata/webapi/photo/getPhotoList?pageth={}&key={}".format(path_th, token))
        r_json = response.json()
        insert_data(r_json['data'])
        while r_json['result'] == "0":
            response = requests.get(
                'http://data1.library.sh.cn/shnh/dydata/webapi/photo/getPhotoList?pageth={}&key={}'.format(
                    path_th, token))
            r_json = response.json()
            insert_data(r_json['data'])
            path_th += 1
            sleep(0.5)

