from rest_framework import serializers
from ddextra.models import TravelPath, RichTextArticle


class TravelPathSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TravelPath
        fields = [
            '_id',
            'name',
            'image',
            'method',
            'duration',
            'feature',
            'longitude',
            'latitude',
            'path_points',
        ]


class RichTextArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = RichTextArticle
        fields = [
            '_id',
            'title',
            'body',
        ]