from django.http import JsonResponse
from django.shortcuts import render

import requests

import os
from ddproj import settings

def profile(request):
    data = {
        'debug': settings.DEBUG,
        'media_root': settings.MEDIA_ROOT,
        'static_root': settings.STATIC_ROOT,
        'env': os.environ.get('DD_BACKEND_ENV')
    }
    return JsonResponse(data)


def libapi(request):
    response = requests.get()
    return JsonResponse({})
