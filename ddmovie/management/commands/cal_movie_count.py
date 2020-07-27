from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddmovie.models import Movie, MoviePeople, MoviePeopleRelation


class Command(BaseCommand):
    help = 'Fix movie data from Library'

    def cal_movie_people_data(self, peopleList, rule_type, movie_uri):
        for people in peopleList:
            pUri = people['puri']
            if not pUri:
                print('pUri not exist ({})'.format(pUri))
                continue
            movie_people = MoviePeople.objects.get(uri=pUri)
            if movie_people:
                movie_people_relation, created = MoviePeopleRelation.objects.get_or_create(
                    movie_uri=movie_uri,
                    people_uri=pUri,
                    rule_type=rule_type
                )
                print(movie_people_relation, created)

    def handle(self, *args, **options):
        movies = Movie.objects.all()
        for movie in movies:
            if movie.raw:
                if movie.raw['directorList']:
                    self.cal_movie_people_data(movie.raw['directorList'], 'director', movie.uri)
                if movie.raw['actorList']:
                    self.cal_movie_people_data(movie.raw['actorList'], 'actor', movie.uri)
                if movie.raw['screenWriterList']:
                    self.cal_movie_people_data(movie.raw['screenWriterList'], 'screenWriter', movie.uri)
