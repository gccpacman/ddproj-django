from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ddpeotry.models import Peotry
from ddpeotry.tasks import get_peotry
from django.db.models import Model

class RamdomPeotryView(APIView):

    def get(self, request):
        first_word = request.query_params.get('str', '')
        if not first_word:
            return Response({
                'status': 'failed',
            })
        try:
            peotry = Peotry.objects.get(
                firstWord=first_word,
                status=1,
            )
            if peotry.status == 1:
                return Response({
                    'status': 'success',
                    'result': peotry.result
                })
            else:
                return Response({
                    'status': 'inqueue',
                    'taskId': peotry.taskId
                })
        except Model.DoesNotExist:
            pass
        peotry_task = get_peotry.delay(first_word)
        Peotry.objects.create(
            firstWord=first_word,
            status=0,
            taskId=peotry_task.id
        )
        return Response({
            'status': 'inqueue',
            'taskId': peotry_task.id
        })
