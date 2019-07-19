from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers, serializers, generics
from rest_framework.response import Response
from rest_framework.urlpatterns import format_suffix_patterns

from ddsrc.models import Road


class RoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Road
        fields = ['name_chs', 'name_en', 'des', 'des2', 'lib_uri', 'temporal_value', \
            'name_after', 'history_of_name', 'history_of_lib_uri', 'place_name', 'place_uri', \
             'is_from_lib', 'lib_update_time', 'update_time', 'create_time',]

class RoadListView(generics.ListAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class RoadDetailsView(generics.RetrieveAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer


urlpatterns = [
    url(r'^roads/$', RoadListView.as_view(), name="road_list"),
    url(r'^roads/(?P<pk>[0-9]+)/$',
        RoadDetailsView.as_view(), name="road_details"),
]

urlpatterns = format_suffix_patterns(urlpatterns)