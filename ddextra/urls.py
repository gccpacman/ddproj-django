from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ddextra.views import RichTextView, TravelPathListView, TravelPathView

urlpatterns = [
    url(r'^travelpaths/$', TravelPathListView.as_view(), name="paths"),
    url(r'^travelpath/(?P<pk>[0-9]+)/$', TravelPathView.as_view(), name="path"),
    url(r'^richtext/(?P<pk>[0-9]+)/$', RichTextView.as_view(), name="richtext"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
