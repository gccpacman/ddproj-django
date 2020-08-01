from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from ddsrc.models import Road, Architecture,Event
from ddsrc.serializer import RoadSerializer, ArchitectureSerializer, EventSerializer


class RoadListView(generics.ListAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'name_chs',
    ]
    ordering_fields = ('architectures_count',)


class RoadDetailsView(generics.RetrieveAPIView):
    queryset = Road.objects.all()
    serializer_class = RoadSerializer


class ArchitectureListView(generics.ListAPIView):
    queryset = Architecture.objects.filter(hidden=False)
    serializer_class = ArchitectureSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_chs', 'road_name_chs']
    filterset_fields = [
        'road_name_chs',
    ]


class ArchitectureDetailView(generics.RetrieveAPIView):
    queryset = Architecture.objects.filter(hidden=False)
    serializer_class = ArchitectureSerializer


class RoadFilterView(APIView):

    def get(self, request):
        road_list = [road.name_chs for road in Road.objects.all()]
        return Response(road_list)


class ArchitectureFilterView(APIView):

    def get(self, request):
        architecture_list = [
            architecture.name_chs
            for architecture in Architecture.objects.filter(hidden=False)
        ]
        return Response(architecture_list)


class ArchitecturePositionsView(APIView):

    def get(self, request):
        place_name = request.query_params.get('place_name')
        if place_name:
            arch_query_list = Architecture.objects.filter(
                hidden=False
            ).filter(
                place_name=place_name
            )
        else:
            arch_query_list = Architecture.objects.filter(hidden=False)
        architecture_list = [{
            "id": arch._id,
            "name": arch.name_chs,
            "title": arch.name_chs,
            "place_name": arch.place_name,
            "value": [arch.longitude, arch.latitude, '100'],
            "latitude": arch.latitude,
            "longitude": arch.longitude,
        } for arch in arch_query_list]
        return Response(architecture_list)


class RoadRelatedPlacesView(APIView):

    def get(self, request):
        place_name = request.query_params.get('place_name')
        if place_name:
            road_query_list = Road.objects.exclude(related_place=None).filter(
                place_name=place_name)
        else:
            road_query_list = Road.objects.exclude(related_place=None).all()
        road_list = [{
            'name': road.name_chs,
            'id': road._id,
            'related_place': road.related_place,
            'related_place_province': road.related_place_province
        } for road in road_query_list]
        return Response(road_list)


class RoadPolylinesView(APIView):

    def get(self, request):
        place_name = request.query_params['place_name']
        road_list = [{
            'road_name': road.name_chs,
            'polylines': road.polylines_bmap
        } for road in Road.objects.filter(place_name=place_name).exclude(
            polylines_bmap={})]
        return Response(road_list)


class PlaceRelatedProvincesCount(APIView):

    def get(self, request):
        place_related_pair_list = [
            place_related_pair for place_related_pair in Road.objects.exclude(
                place_name2=None).exclude(related_place_province=None)
            .values('place_name2', 'related_place_province').annotate(
                related_place_province_count=Count('related_place_province')
            ).order_by('related_place_province_count')
        ]
        links = []
        for place_related_pair in place_related_pair_list:
            links.append({
                'source': place_related_pair['place_name2'],
                'target': place_related_pair['related_place_province'],
                'value': place_related_pair['related_place_province_count']
            })
        return Response(links)



class EventListView(generics.ListAPIView):
    queryset = Event.objects.all().order_by("_id")
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = [
        'event_title',
    ]
    filterset_fields = [
        'event_begin',
        'event_end',
    ]


class EventDetailsView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ThatYearView(APIView):

    def get(self, request):
        event_begin_month = request.query_params.get('month')
        event_begin_day = request.query_params.get('day')
        if not event_begin_month or not event_begin_day:
            return Response([])
        events =  Event.objects.filter(event_begin__month=event_begin_month, event_begin__day=event_begin_day).order_by("event_begin")
        event_list = []
        for event in events:
            event_list.append({
                "event_title": event.event_title,
                "event_image_path": event.event_image.url if event.event_image else '',
                "event_begin": event.event_begin,
                "event_end": event.event_end
            })
        return Response(event_list)