from django.shortcuts import render
from rest_framework import serializers, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from ddmovie.models import Movie, MoviePeople, MovieCinema


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
        ]

class MovieSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Movie
        fields = [
            '_id',
            'name',
            'pub_date',
            'uri',
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
            'raw',
        ]

class MovieCinemaListView(generics.ListAPIView):
    queryset = MovieCinema.objects.all()
    serializer_class = MovieCinemaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]


class MovieCinemaDetailsView(generics.RetrieveAPIView):
    queryset = MovieCinema.objects.all()
    serializer_class = MovieCinemaSerializer

class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]


class MovieDetailsView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MoviePeopleListView(generics.ListAPIView):
    queryset = MoviePeople.objects.all()
    serializer_class = MoviePeopleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]


class MoviePeopleDetailsView(generics.RetrieveAPIView):
    queryset = MoviePeople.objects.all()
    serializer_class = MoviePeopleSerializer
