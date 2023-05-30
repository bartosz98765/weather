from datetime import datetime

from django.http import JsonResponse
from django.views import View

from backend.models import Location, CurrentWeather, DailyWeather
from backend.tests import EXPECTED_WEATHER_DATA
from backend.weatherapi_adapter import WeatherApiAdapter


class MainView(View):
    def get(self, request, city: str):
        now = datetime.now()
        result = WeatherApiAdapter().get_forecast(city)

        context = {
            "location": result["location"],
            "current": result["current"],
            "daily": self.__get_daily_weather(name=city, now=now),
        }
        return JsonResponse(context, safe=False)


    def __get_daily_weather(self, name: str, now: datetime):
        # daily = DailyWeather.objects.get_or_create(name=name)
        daily = EXPECTED_WEATHER_DATA["daily"]
        return daily
