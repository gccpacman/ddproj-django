from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ddmovie.views import (
    MovieCinemaListView,
    MoviePeopleListView,
    MovieCinemaDetailsView,
    MoviePeopleDetailsView,
    MovieListView,
    MovieDetailsView,
)

urlpatterns = [
    url(r'^cinemas/$', MovieCinemaListView.as_view(), name="cinemas"),
    url(r'^cinema/(?P<pk>[0-9]+)/$', MovieCinemaDetailsView.as_view(), name="cinema"),
    url(r'^peoples/$', MoviePeopleListView.as_view(), name="peoples"),
    url(r'^people/(?P<pk>[0-9]+)/$', MoviePeopleDetailsView.as_view(), name="people"),
    url(r'^movies/$', MovieListView.as_view(), name="movies"),
    url(r'^movie/(?P<pk>[0-9]+)/$', MovieDetailsView.as_view(), name="movie"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
