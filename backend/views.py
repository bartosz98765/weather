from datetime import datetime, timedelta

from django.http import JsonResponse
from django.views import View

from backend.models import CurrentWeather, DailyWeather, Location
from backend.weatherapi_adapter import WeatherApiAdapter
from weather.settings import DATA_VALIDITY_HOURS


class MainView(View):
    def get(self, request, city: str):
        now = datetime.now()
        data_validity_time = now - timedelta(hours=DATA_VALIDITY_HOURS)

        location, location_created = Location.objects.get_or_create(name=city)
        if location_created:
            past_day_no = 5
            forecast = WeatherApiAdapter().get_forecast(city)
            daily = self.__get_daily_weather(city, now, past_day_no)
            daily.extend(forecast["forecast_daily"])

            updated = Location.objects.update(**forecast["location"])


        context = {
            "location": forecast["location"],
            "current": forecast["current"],
            "daily": daily,
        }
        return JsonResponse(context, safe=False)

    @staticmethod
    def __get_daily_weather(city: str, now: datetime, past_day_count: int):
        # daily = DailyWeather.objects.get_or_create(name=name)
        daily = []
        for i in range(past_day_count, 0, -1):
            past_day = (now - timedelta(i)).strftime("%Y-%m-%d")
            history = WeatherApiAdapter().get_history_day(city, past_day)
            if history:
                daily.append(history)
        return daily
