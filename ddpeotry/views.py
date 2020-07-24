from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from ddpeotry.poetry.dataset import PeotryTokenizer
from ddpeotry.poetry.model import get_model
from ddpeotry.poetry import utils
from ddproj import settings

class RamdomPeotryView(APIView):

    def get(self, request):
        peotryTokenizer = PeotryTokenizer()
        model = get_model(peotryTokenizer.get_keep_words())
        model.load_weights(settings.BEST_MODEL_PATH)
        return Response(utils.generate_random_poetry(peotryTokenizer.get_tokenizers(), model, s='今天很沮丧'))
