from rest_framework import serializers, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView

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
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'event_title',
    ]


class EventDetailsView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
