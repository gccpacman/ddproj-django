from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddmovie.models import MoviePhoto, MoviePeople, MoviePhotoPeople


class Command(BaseCommand):
    help = 'Fetching photo data from Library'

    def handle(self, *args, **options):
        moviePhotos = MoviePhoto.objects.all()

        for moviePhoto in moviePhotos:
            moviePhoto.movieUri = moviePhoto.raw.get('movie')
            moviePhoto.movieName = moviePhoto.raw.get('movieName')
            if moviePhoto.raw.get('personList') and len(moviePhoto.raw['personList']) > 0:
                for person in moviePhoto.raw['personList']:
                    puri = person['puri']
                    moviePeoples = MoviePeople.objects.filter(uri=puri)
                    if moviePeoples:
                        moviePeople = moviePeoples[0]
                        moviePhotoPeople, created = MoviePhotoPeople.objects.get_or_create(
                            photoUri=moviePhoto.uri,
                            peopleUri=puri,
                            peopleName=moviePeople.name
                        )
            moviePhoto.save()
