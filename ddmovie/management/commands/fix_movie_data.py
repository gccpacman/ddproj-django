from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddmovie.models import Movie


class Command(BaseCommand):
    help = 'Fix movie data from Library'

    def handle(self, *args, **options):
        movies = Movie.objects.all()
        for movie in movies:
            formated_pub_date = movie.pub_date.replace('s', '').split('-')[0].strip()
            movie.formated_pub_date = formated_pub_date
            movie.save()
