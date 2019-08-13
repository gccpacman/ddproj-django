from django.shortcuts import render
from django.db.models import Count
from rest_framework import routers, serializers, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from ddsrc.models import Road, Architecture


class ArchitectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Architecture
        fields = ['_id', 'name_chs', 'name_cht', 'name_en', 'des2', 'des_html', 'road', 'road_name_chs', 'road_lib_uri', \
             'address', 'house_number', 'longitude', 'latitude', \
            'place_name_str', 'place_uri', 'batch_no', 'first_image_path', ]


class RoadSerializer(serializers.ModelSerializer):
    road_architecture = ArchitectureSerializer(many=True)
    road_architecture_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Road
        fields = ['_id', 'name_chs', 'name_en', 'des', 'des2', 'des_html', 'lib_uri', 'temporal_value', \
             'name_after', 'history_of_name', 'history_of_lib_uri', \
             'road_architecture', 'road_architecture_count', 'polylines_bmap', 'center_bmap',  'place_name', 'place_name2', ]


class RoadListView(generics.ListAPIView):
    queryset = Road.objects.annotate(road_architecture_count=Count('road_architecture'))
    serializer_class = RoadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter,]
    search_fields = ['name_chs', ]
    ordering_fields = ('road_architecture_count',)

class RoadDetailsView(generics.RetrieveAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer

class ArchitectureListView(generics.ListAPIView):
    queryset = Architecture.objects.all()
    serializer_class = ArchitectureSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name_chs', 'road_name_chs' ]
    filterset_fields = ['road_name_chs', ]

class ArchitectureDetailView(generics.RetrieveAPIView):
    queryset = Architecture.objects.all()
    serializer_class = ArchitectureSerializer

class RoadFilterView(APIView):
    def get(self, request):
        road_list = [road.name_chs for road in Road.objects.all()]
        return Response(road_list)

class ArchitectureFilterView(APIView):
    def get(self, request):
        architecture_list = [architecture.name_chs for architecture in Architecture.objects.all()]
        return Response(architecture_list)

class ArchitectureFilterView(APIView):
    def get(self, request):
        architecture_list = [architecture.name_chs for architecture in Architecture.objects.all()]
        return Response(architecture_list)

class ArchitecturePositionsView(APIView):
    def get(self, request):
        place_name = request.query_params.get('place_name')
        if place_name:
            arch_query_list = Architecture.objects.filter(place_name=place_name)
        else:
            arch_query_list = Architecture.objects.all()
        architecture_list = [{"id": arch._id, "name": arch.name_chs, "place_name": arch.place_name, "value": [ arch.longitude,  arch.latitude, '100']} for arch in arch_query_list]
        return Response(architecture_list)

class RoadRelatedPlacesView(APIView):
    def get(self, request):
        place_name = request.query_params.get('place_name')
        if place_name:
            road_query_list = Road.objects.exclude(related_place=None).filter(place_name=place_name)
        else:
            road_query_list = Road.objects.exclude(related_place=None).all()
        road_list = [{'name': road.name_chs, 'id': road._id, 'related_place': road.related_place, 'related_place_province': road.related_place_province } for road in road_query_list]
        return Response(road_list)

class RoadPolylinesView(APIView):
    def get(self, request):
        place_name = request.query_params['place_name']
        road_list = [{'road_name': road.name_chs, 'polylines': road.polylines_bmap} for road in Road.objects.filter(place_name=place_name).exclude(polylines_bmap={})]
        return Response(road_list)

class PlaceRelatedProvincesCount(APIView):
    def get(self, request):
        place_related_pair_list = [place_related_pair for place_related_pair in Road.objects.exclude(place_name2=None).exclude(related_place_province=None).values('place_name2', 'related_place_province').annotate(related_place_province_count=Count('related_place_province')).order_by('related_place_province_count')]
        links = []
        for place_related_pair in place_related_pair_list:
            links.append({
                'source': place_related_pair['place_name2'],
                'target': place_related_pair['related_place_province'],
                'value': place_related_pair['related_place_province_count']
            })
        return Response(links)
