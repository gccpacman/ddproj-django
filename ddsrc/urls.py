from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ddsrc.views import (RoadListView, RoadDetailsView, ArchitectureListView,
                         ArchitectureDetailView, RoadFilterView,
                         ArchitectureFilterView, RoadPolylinesView,
                         RoadRelatedPlacesView, ArchitecturePositionsView,
                         PlaceRelatedProvincesCount)

urlpatterns = [
    url(r'^roads/$', RoadListView.as_view(), name="road-list"),
    url(r'^road/(?P<pk>[0-9]+)/$', RoadDetailsView.as_view(), name="road-detail"),
    url(r'^architectures/$', ArchitectureListView.as_view(), name="architecture-list"),
    url(r'^architecture/(?P<pk>[0-9]+)/$', ArchitectureDetailView.as_view(), name="architecture-detail"),
    url(r'^keyword/road$', RoadFilterView.as_view(), name="keyword-road"),
    url(r'^keyword/architecture$', ArchitectureFilterView.as_view(), name="keyword-architecture"),
    url(r'^road/polylines/$', RoadPolylinesView.as_view(), name="road-polylines"),
    url(r'^road/relatedplaces/$', RoadRelatedPlacesView.as_view(), name="road-relatedplaces"),
    url(r'^architecture/positions/$', ArchitecturePositionsView.as_view(), name="architecture-positons"),
    url(r'^place/relatedprovinces/$', PlaceRelatedProvincesCount.as_view(), name="place-releated-provinces"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
