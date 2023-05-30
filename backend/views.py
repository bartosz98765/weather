from datetime import datetime, timedelta

from django.http import JsonResponse
from django.views import View

from backend.models import CurrentWeather, DailyWeather, Location
from backend.weatherapi_adapter import WeatherApiAdapter


class MainView(View):
    def get(self, request, city: str):
        now = datetime.now()
        forecast = WeatherApiAdapter().get_forecast(city)
        past_day_no = 5

        daily = self.__get_daily_weather(city, now, past_day_no)
        daily.extend(forecast["forecast_daily"])

        context = {
            "location": forecast["location"],
            "current": forecast["current"],
            "daily": daily,
        }
        return JsonResponse(context, safe=False)

    def __get_daily_weather(self, city: str, now: datetime, past_day_count: int):
        # daily = DailyWeather.objects.get_or_create(name=name)
        daily = []
        for i in range(past_day_count, 0, -1):
            past_day = (now - timedelta(i)).strftime("%Y-%m-%d")
            history = WeatherApiAdapter().get_history_day(city, past_day)
            if history:
                daily.append(history)
        return daily
