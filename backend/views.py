from django.http import JsonResponse
from django.views.generic import ListView

from backend.tests import EXPECTED_WEATHER_DATA


class MainView(ListView):
    def get_queryset(self):
        return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["location"] = EXPECTED_WEATHER_DATA["location"]
        context["current"] = EXPECTED_WEATHER_DATA["current"]
        context["daily"] = EXPECTED_WEATHER_DATA["daily"]
        return context

    def render_to_response(self, context, **response_kwargs):
        weather_data = self.__get_data(context)
        return JsonResponse(weather_data, safe=False)

    @staticmethod
    def __get_data(context):
        weather_data = {"location": context["location"]}
        weather_data.update({"current": context["current"]})
        weather_data.update({"daily": context["daily"]})
        return weather_data
