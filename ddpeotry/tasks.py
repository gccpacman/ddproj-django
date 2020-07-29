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
    Peotry.objects.create(
        firstWord=first_word,
        result=result
    )
    return result