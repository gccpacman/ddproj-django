from django.shortcuts import render
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from ddmovie.models import Movie, MoviePeople, MoviePhoto, MoviePhotoPeople, MovieCinema
from ddmovie.serializer import MovieSerializer, MoviePeopleSerializer, MovieCinemaSerializer


class MovieCinemaListView(generics.ListAPIView):
    queryset = MovieCinema.objects.all().order_by("_id")
    serializer_class = MovieCinemaSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]
    ordering_fields = ('_id',)


class MovieCinemaDetailsView(generics.RetrieveAPIView):
    queryset = MovieCinema.objects.all()
    serializer_class = MovieCinemaSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all().order_by("_id")
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]
    ordering_fields = ('_id',)


class MovieDetailsView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoviePeopleListView(generics.ListAPIView):
    queryset = MoviePeople.objects.all().order_by("_id")
    serializer_class = MoviePeopleSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name',
    ]
    ordering_fields = ('_id',)


class MoviePeopleDetailsView(generics.RetrieveAPIView):
    queryset = MoviePeople.objects.all()
    serializer_class = MoviePeopleSerializer


class MovieTimelineView(APIView):
    def get(self, request):
        movies_queryset = Movie.objects.order_by("formated_pub_date")
        movie_by_year = {}
        for movie in movies_queryset:
            formated_pub_date = movie.formated_pub_date
            movie_by_year[formated_pub_date].append({
                "_id": movie._id,
                "name": movie.name,
                "uri": movie.uri,
                "pub_date": movie.pub_date,
                "movie_type": movie.movie_type,
                "first_image_path": movie.first_image_path,
            })
        return Response(movie_by_year)