from rest_framework import serializers, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from ddsrc.models import Event

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = [
            '_id',
            'event_title',
            'event_image',
            'event_begin',
            'event_end',
            'uri',
            'raw',
        ]


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