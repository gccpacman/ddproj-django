import requests
from django.core.management.base import BaseCommand

from simplejson.errors import JSONDecodeError

from ddproj.settings import SHANGHAI_LIBRARY_API_KEY as token
from ddmovie.models import Movie, MoviePeople


def insert_people(peopleList):
    for people in peopleList:
        pUri = people['puri']
        if not pUri:
            print('pUri not exist ({})'.format(pUri))
            continue
        url = "http://data1.library.sh.cn/shnh/dydata/webapi/person/personDetailAll?uri={}&key={}".format(pUri, token)
        response = requests.get(url)
        if response.status_code != 200:
            print('response status code not 200. ({})'.format(pUri))
            continue
        try:
            rJson = response.json()
            mPeople, created = MoviePeople.objects.get_or_create(uri=pUri)
            if created and rJson.get('personDetail') and len(rJson.get('personDetail')) > 0:
                personDetail = rJson['personDetail'][0]
                mPeople.name = personDetail.get('chs_name', "")
                mPeople.uri = pUri
                mPeople.raw = rJson
                mPeople.speciality = personDetail.get('speciality', "")
                mPeople.nationality = personDetail.get('nationality', "")
                mPeople.save()
                print('{} {}'.format(mPeople.name, mPeople.uri))
        except JSONDecodeError as e:
            print(pUri, response.raw)
            break


class Command(BaseCommand):
    help = 'Fetching movie people data from Library'

    def handle(self, *args, **options):
        movies = Movie.objects.all()
        for movie in movies:
            # print(movie['directorList'])
            if movie.raw:
                if movie.raw['directorList']:
                    insert_people(movie.raw['directorList'])
                if movie.raw['actorList']:
                    insert_people(movie.raw['actorList'])
                if movie.raw['screenWriterList']:
                    insert_people(movie.raw['screenWriterList'])
