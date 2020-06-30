from django.http import JsonResponse
from django.shortcuts import render

import requests


def profile(request):
    data = {
        'name': 'Vitor',
        'location': 'Finland',
        'is_active': True,
        'count': 28
    }
    return JsonResponse(data)


def libapi(request):
    response = requests.get()
    return JsonResponse({})
