from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from ddpeotry.views import RamdomPeotryView

urlpatterns = [
    url(r'^generate/$', RamdomPeotryView.as_view(), name="ramdom-peotry"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
