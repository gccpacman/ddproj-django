from io import BytesIO
from django.core.management.base import BaseCommand
from django.core.files.base import File
import requests

from ddmovie.models import Movie, MoviePeople
from ddsrc.models import Event, EventRelation, Architecture


class Command(BaseCommand):
    help = 'Fix movie data from Library'

    def handle(self, *args, **options):
        for movie in Movie.objects.all():
            movie.event_count = EventRelation.objects.filter(relation_type='movie').filter(relation_uri=movie.uri).count()
            movie.save()
    
        for movie_people in MoviePeople.objects.all():
            movie_people.event_count = EventRelation.objects.filter(relation_type='person').filter(relation_uri=movie_people.uri).count()
            movie_people.save()

        for architecture in Architecture.objects.filter(hidden=False):
            architecture.event_count = EventRelation.objects.filter(relation_type='place').filter(relation_uri=architecture.lib_uri).count()
            architecture.save()