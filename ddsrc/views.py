from django.shortcuts import render
from rest_framework import routers, serializers, generics, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from ddsrc.models import Road, Architecture


class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = ['_id', 'name_chs', 'name_en', 'des', 'des2', 'lib_uri', 'temporal_value', \
             'name_after', 'history_of_name', 'history_of_lib_uri', 'place_name', 'place_uri', \
             'polylines_bmap', 'polylines_gaode', \
             'is_from_lib', 'lib_update_time', 'update_time', 'create_time',]

class ArchitectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Architecture
        fields = ['_id', 'name_chs', 'name_cht', 'name_en', 'des', 'des2', 'road', 'road_name_chs', 'road_lib_uri', \
             'address', 'house_number', 'longitude', 'latitude', 'is_from_lib', 'protect_type', \
             'lib_uri', 'place_name', 'place_uri', 'batch_no', 'first_image_uri', 'first_image_path','first_image_lib_uri', \
             'lib_is_red', 'lib_update_time', 'update_time', 'create_time', ]


class RoadListView(generics.ListAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_chs', 'name_en', 'place_name']

class RoadDetailsView(generics.RetrieveAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class ArchitectureListView(generics.ListAPIView):
    queryset = Architecture.objects.all()
    serializer_class = ArchitectureSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name_chs', 'name_cht', 'name_en', 'road_name_chs', 'place_name']
    filterset_fields = ['road_name_chs', ]

class ArchitectureDetailView(generics.RetrieveAPIView):
    queryset = Architecture.objects.all()
    serializer_class = ArchitectureSerializer
