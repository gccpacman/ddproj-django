from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ddpeotry.poetry.dataset import PeotryTokenizer
from ddpeotry.poetry.model import get_model
from ddpeotry.poetry import utils
from ddpeotry.models import Peotry
from ddproj import settings


class RamdomPeotryView(APIView):

    def get(self, request):
        first_word = request.query_params.get('str', '')
        if not first_word:
            return
        peotry = Peotry.objects.filter(firstWord=first_word)
        if len(peotry) > 0:
            return Response(peotry.result)
        peotryTokenizer = PeotryTokenizer()
        model = get_model(peotryTokenizer.get_keep_words())
        model.load_weights(settings.BEST_MODEL_PATH)
        return Response(utils.generate_random_poetry(peotryTokenizer.get_tokenizers(), model, s=first_word))
