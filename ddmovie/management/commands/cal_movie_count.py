from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddmovie.models import Movie, MoviePeople


class Command(BaseCommand):
    help = 'Fix movie data from Library'

    def cal_movie_people_data(self, peopleList, people_type):
        for people in peopleList:
            pUri = people['puri']
            if not pUri:
                print('pUri not exist ({})'.format(pUri))
                continue
            movie_people = MoviePeople.objects.get(uri=pUri)
            if movie_people:
                if people_type == 'director':
                    movie_people.director_count += 1
                elif people_type == 'actor':
                    movie_people.movie_count += 1
                else:
                    movie_people.screenwriter_count += 1
                movie_people.save()

    def handle(self, *args, **options):
        movies = Movie.objects.all()
        for movie in movies:
            for movie in movies:
                if movie.raw:
                    if movie.raw['directorList']:
                        self.cal_movie_people_data(movie.raw['directorList'], 'director')
                    if movie.raw['actorList']:
                        self.cal_movie_people_data(movie.raw['actorList'], 'actor')
                    if movie.raw['screenWriterList']:
                        self.cal_movie_people_data(movie.raw['screenWriterList'], 'screenWriter')
