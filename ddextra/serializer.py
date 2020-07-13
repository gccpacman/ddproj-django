from rest_framework import serializers
from ddextra.models import TravelPath


class MovieCinemaSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TravelPath
        fields = [
            '_id',
            'name'
            'method',
            'duration',
            'feature',
        ]