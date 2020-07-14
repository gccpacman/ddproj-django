from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render

from ddextra.serializer import TravelPathSerializer, RichTextArticleSerializer
from ddextra.models import TravelPath, RichTextArticle


class TravelPathListView(generics.ListAPIView):
    queryset = TravelPath.objects.all().order_by("_id")
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'title',
    ]
    serializer_class = TravelPathSerializer


class TravelPathView(generics.RetrieveAPIView):
    queryset = TravelPath.objects.all()
    serializer_class = TravelPathSerializer


class RichTextView(generics.RetrieveAPIView):
    queryset = RichTextArticle.objects.all()
    serializer_class = RichTextArticleSerializer