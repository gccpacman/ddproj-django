from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers, serializers, generics
from rest_framework.response import Response

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

class RoadDetailView(generics.RetrieveAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

urlpatterns = [
    url(r'^roads/$', RoadListView.as_view()),
    url(r'^roads/<int:pk>/$', RoadDetailView.as_view()),
]