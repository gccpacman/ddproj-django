from rest_framework import serializers
from ddextra.models import TravelPath, RichTextArticle


class TravelPathSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TravelPath
        fields = [
            '_id',
            'name',
            'method',
            'duration',
            'feature',
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