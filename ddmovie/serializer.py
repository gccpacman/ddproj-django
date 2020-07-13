from rest_framework import serializers
from ddmovie.models import Movie, MoviePeople, MoviePhoto, MoviePhotoPeople, MovieCinema


class MovieCinemaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MovieCinema
        fields = [
            '_id',
            'name',
            'nameEn',
            'uri',
            'architectureUri',
            'raw',
            'longitude',
            'latitude',
            'related_people',
            'related_event',
        ]


class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = [
            '_id',
            'name',
            'pub_date',
            'uri',
            'detail_raw',
            'directors',
            'actors',
            'first_image_path',
            'raw',
        ]


class MoviePeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MoviePeople
        fields = [
            '_id',
            'name',
            'speciality',
            'nationality',
            'uri',
            'first_image_path',
            'raw',
        ]
