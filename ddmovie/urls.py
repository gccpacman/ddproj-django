from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ddmovie.views import (MovieCinemaListView, MoviePeopleListView, MovieCinemaDetailsView,
    MoviePeopleDetailsView, MovieListView,MovieDetailsView,MovieTimelineView, MovieCinemaPositionsView)
from ddsrc.views import (ArchitectureListView, ArchitectureDetailView, ArchitecturePositionsView,
    EventListView, EventDetailsView, ThatYearView)


urlpatterns = [
    url(r'^peoples/$', MoviePeopleListView.as_view(), name="peoples"),
    url(r'^people/(?P<pk>[0-9]+)/$', MoviePeopleDetailsView.as_view(), name="people"),
    url(r'^movies/$', MovieListView.as_view(), name="movies"),
    url(r'^movie/(?P<pk>[0-9]+)/$', MovieDetailsView.as_view(), name="movie"),
    url(r'^cinemas/$', MovieCinemaListView.as_view(), name="cinemas"),
    url(r'^cinema/(?P<pk>[0-9]+)/$', MovieCinemaDetailsView.as_view(), name="cinema"),
    url(r'^buildings/$', ArchitectureListView.as_view(), name="architecture-list"),
    url(r'^building/(?P<pk>[0-9]+)/$', ArchitectureDetailView.as_view(), name="architecture-detail"),
    url(r'^events/$', EventListView.as_view(), name="events"),
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetailsView.as_view(), name="event"),
    url(r'^timeline/$', MovieTimelineView.as_view(), name="timeline"),
    url(r'^thatyear/', ThatYearView.as_view(), name="thatyear"),
    url(r'^position/cinema/$', MovieCinemaPositionsView.as_view(), name="cinema_position"),
    url(r'^position/building/$', ArchitecturePositionsView.as_view(), name="architecture-positons"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
