from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ddsrc.app_views import EventListView, EventDetailsView

urlpatterns = [
    url(r'^events/$', EventListView.as_view(), name="events"),
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetailsView.as_view(), name="event"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
