from datetime import datetime

from django.http import JsonResponse
from django.views import View

from backend.models import Location, CurrentWeather, DailyWeather
from backend.tests import EXPECTED_WEATHER_DATA


class MainView(View):
    def get(self, request, city: str):
        now = datetime.now()

        context = {
            "location": self.__get_location(name=city, now=now),
            "current": self.__get_current_weather(name=city, now=now),
            "daily": self.__get_daily_weather(name=city, now=now),
        }
        return JsonResponse(context, safe=False)

    def __get_location(self, name: str, now: datetime):
        # location = Location.objects.get_or_create(name=name)
        location = EXPECTED_WEATHER_DATA["location"]
        return location

    def __get_current_weather(self, name: str, now: datetime):
        # current = CurrentWeather.objects.get_or_create(name=name)
        current = EXPECTED_WEATHER_DATA["current"]
        return current

    def __get_daily_weather(self, name: str, now: datetime):
        # daily = DailyWeather.objects.get_or_create(name=name)
        daily = EXPECTED_WEATHER_DATA["daily"]
        return daily
