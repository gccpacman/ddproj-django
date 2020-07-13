from rest_framework import serializers
from ddsrc.models import Road, Architecture, Event


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


class ArchitectureSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Architecture
        fields = [
            '_id',
            'name_chs',
            'name_cht',
            'name_en',
            'des2',
            'des_html',
            'road',
            'road_name_chs',
            'road_lib_uri',
            'address',
            'house_number',
            'longitude',
            'latitude',
            'place_name_str',
            'place_uri',
            'batch_no',
            'first_image_path',
            'related_people',
            'related_event'
        ]


class RoadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Road
        fields = [
            '_id',
            'name_chs',
            'name_en',
            'des',
            'des2',
            'des_html',
            'lib_uri',
            'temporal_value',
            'name_after',
            'history_of_name',
            'history_of_lib_uri',
            'place_name',
            'place_name2',
            'architectures_list',
            'architectures_count',
            # 'polylines_bmap',
        ]



