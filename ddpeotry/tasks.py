from __future__ import absolute_import, unicode_literals

from celery import shared_task

from ddpeotry.utils import generate_random_poetry
from ddpeotry.models import Peotry

@shared_task
def add(x, y):
    return x + y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def get_peotry(first_word):
    result = generate_random_poetry(
        s=first_word
    )
    try:
        peotry = Peotry.objects.get(
            firstWord=first_word,
            status=0
        )
        peotry.result = result
        peotry.status = 1
        peotry.save()
    except Peotry.DoesNotExist:
        pass
    return result