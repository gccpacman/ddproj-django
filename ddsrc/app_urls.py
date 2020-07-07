from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ddsrc.app_views import EventListView, EventDetailsView, ThatYearView

urlpatterns = [
    url(r'^events/$', EventListView.as_view(), name="events"),
    url(r'^event/(?P<pk>[0-9]+)/$', EventDetailsView.as_view(), name="event"),
    url(r'^thatyear/', ThatYearView.as_view(), name="thatyear"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
