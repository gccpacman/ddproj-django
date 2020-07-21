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
            'longitude',
            'latitude',
            'des_html',
            'first_image_path',
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
            'directors',
            'event_count',
            'actors',
            'lib_image_path',
            'des_html',
            'first_image_path',
            'related_photo',
        ]


class MoviePeopleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MoviePeople
        fields = [
            '_id',
            'name',
            'speciality',
            'nationality',
            'nativeplace',
            'uri',
            'event_count',
            'movie_count',
            'screenwriter_count',
            'director_count',
            'first_image_path',
            'des_html',
            'birthday',
            'deathday',
            'related_movie',
            'related_photo',
        ]
