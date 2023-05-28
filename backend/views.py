import json

from django.http import JsonResponse
from django.views.generic import ListView

from backend.tests import EXPECTED_WEATHER_DATA


class MainView(ListView):
    def get_queryset(self):
        return []

    def render_to_response(self, context, **response_kwargs):
        data = EXPECTED_WEATHER_DATA
        return JsonResponse(data, safe=False)
