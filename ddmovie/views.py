from django.shortcuts import render
from rest_framework import serializers, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from ddmovie.models import Movie, MoviePeople, MoviePhoto, MoviePhotoPeople, MovieCinema

class MovieCinemaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = MovieCinema
        fields = [
            '_id',
            'name',
            'nameEn',
            'architectureUri',
        ]