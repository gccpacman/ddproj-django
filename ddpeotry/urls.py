from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ddpeotry.views import RamdomPeotryView, PeotryView

urlpatterns = [
    url(r'^generate/$', RamdomPeotryView.as_view(), name="ramdom-peotry"),
    url(r'^get/$', PeotryView.as_view(), name="peotry"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
