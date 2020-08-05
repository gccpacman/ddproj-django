from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ddpeotry.models import Peotry
from ddpeotry.tasks import get_peotry

class PeotryView(APIView):

    def get(self, request):
        task_id = request.query_params.get('taskId')
        if task_id:
            try:
                peotry = Peotry.objects.get(
                    taskId=task_id
                )
                if peotry.status == 1:
                    return Response({
                        'status': 'success',
                        'message': 'check result',
                        'taskId': peotry.taskId,
                        'result': peotry.result
                    })
                else:
                    return Response({
                        'status': 'inqueue',
                        'message': 'still in queue, please wait',
                        'taskId': peotry.taskId
                    })
            except Peotry.DoesNotExist:
                return Response({
                    'status': 'failed',
                    'message': 'server error'
                })


class RamdomPeotryView(APIView):

    def get(self, request):
        first_word = request.query_params.get('str')
        if not first_word:
            return Response({
                'status': 'failed',
                'message': 'no input'
            })
        peotry_task = get_peotry.delay(first_word)
        Peotry.objects.create(
            firstWord=first_word,
            status=0,
            taskId=peotry_task.id
        )
        return Response({
            'status': 'success',
            'message': 'task started',
            'taskId': peotry_task.id
        })
