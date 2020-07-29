from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ddpeotry.models import Peotry
from ddpeotry.tasks import get_peotry


class RamdomPeotryView(APIView):

    def get(self, request):
        first_word = request.query_params.get('str', '')
        if not first_word:
            return Response({
                'status': 'faild',
            })
        peotry = Peotry.objects.filter(firstWord=first_word)
        if len(peotry) > 0:
            return Response(peotry[0].result)
        peotry_task = get_peotry.delay(first_word)
        return Response({
            'status': 'success',
            'taskId': peotry_task.id
        })
