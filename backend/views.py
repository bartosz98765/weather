from datetime import datetime, timedelta

import pytz as pytz
from django.http import JsonResponse
from django.views import View

from backend.models import CurrentWeather, DailyWeather, Location
from backend.weatherapi_adapter import WeatherApiAdapter
from weather.settings import DATA_VALIDITY_HOURS, HISTORY_MAX_DAYS


class MainView(View):
    def get(self, request, city: str):
        try:
            location = Location.objects.get(name=city)
        except Location.DoesNotExist:
            forecast = WeatherApiAdapter().get_forecast(city)
            location = Location.objects.create(**forecast["location"])
            now = datetime.now(location.timezone)

            current_weather = CurrentWeather.objects.create(
                **forecast["current"], location=location
            )

            history_days = self.__get_daily_weather(city, now)
            forecast_days = forecast["forecast_daily"]
            daily = []
            daily.extend(history_days)
            daily.extend(forecast_days)

            for day in daily:
                DailyWeather.objects.create(**day, location=location)
        else:
            now = datetime.now(tz=pytz.timezone(location.timezone))
            if location.currentweather.last_updated > now - timedelta(
                hours=DATA_VALIDITY_HOURS
            ):
                pass
                # self.__get_location_objects(location)
        context = {
            "location": forecast["location"],
            "current": forecast["current"],
            "daily": daily,
        }
        return JsonResponse(context, safe=False)

    @staticmethod
    def __get_daily_weather(city: str, now: datetime, past_day_count=HISTORY_MAX_DAYS):
        # daily = DailyWeather.objects.get_or_create(name=name)
        daily = []
        for i in range(past_day_count, 0, -1):
            past_day = (now - timedelta(i)).strftime("%Y-%m-%d")
            history = WeatherApiAdapter().get_history_day(city, past_day)
            if history:
                daily.append(history)
        return daily
