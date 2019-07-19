from django.conf.urls import url, include
from ddsrc.models import Road
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

class RoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Road
        fields = ['name_chs', 'name_en', 'des', 'des2', 'lib_uri', 'temporal_value', \
            'name_after', 'history_of_name', 'history_of_lib_uri', 'place_name', 'place_uri', \
             'is_from_lib', 'lib_update_time', 'update_time', 'create_time',]

class RoadViewSet(viewsets.ModelViewSet):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

router = routers.DefaultRouter()
router.register(r'roads', RoadViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]