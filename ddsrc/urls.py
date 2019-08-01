from django.conf.urls import url, include
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ddsrc.views import (
    RoadListView,
    RoadDetailsView,
    ArchitectureListView,
    ArchitectureDetailView,
    RoadFilterView,
    ArchitectureFilterView,
)

urlpatterns = [
    url(r'^roads/$', RoadListView.as_view(), name="road-list"),
    url(r'^road/(?P<pk>[0-9]+)/$', RoadDetailsView.as_view(), name="road-detail"),
    url(r'^architectures/$', ArchitectureListView.as_view(), name="architecture-list"),
    url(r'^architecture/(?P<pk>[0-9]+)/$', ArchitectureDetailView.as_view(), name="architecture-detail"),
    url(r'^keyword/road$', RoadFilterView.as_view(), name="filter-road-name"),
    url(r'^keyword/architecture$', ArchitectureFilterView.as_view(), name="filter-road-name"),
]

urlpatterns = format_suffix_patterns(urlpatterns)