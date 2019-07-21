from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ddsrc.views import (
    RoadListView,
    RoadDetailsView,
    ArchitectureListView,
    ArchitectureDetailView,
)

urlpatterns = [
    url(r'^roads/$', RoadListView.as_view(), name="road-list"),
    url(r'^roads/(?P<pk>[0-9]+)/$', RoadDetailsView.as_view(), name="road-detail"),
    url(r'^architectures/$', ArchitectureListView.as_view(), name="architecture-list"),
    url(r'^architectures/(?P<pk>[0-9]+)/$', ArchitectureDetailView.as_view(), name="architecture-detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)