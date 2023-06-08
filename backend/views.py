from datetime import datetime, timedelta, timezone
from django.http import JsonResponse
from django.views import View
from marshmallow import Schema, fields

from backend.models import CurrentWeather, DailyWeather, Location
from backend.weatherapi_adapter import (
    WeatherApiAdapter,
    CurrentWeatherSchema,
    DailyWeatherSchema,
)
from weather.settings import DATA_VALIDITY_HOURS, HISTORY_MAX_DAYS


class LocationResponseSchema(Schema):
    name = fields.String(required=True)
    country = fields.String(required=True)
    latitude = fields.Float(required=True)
    longitude = fields.Float(required=True)
    timezone = fields.String(required=True)

    class Meta:
        ordered = True


class MainView(View):
    def get(self, request, city: str):
        try:
            location = Location.objects.get(name=city)
        except Location.DoesNotExist:
            context = self.__get_all_weather_data(city)
        else:
            now = (datetime.now()).replace(tzinfo=timezone.utc)
            if location.currentweather.last_updated > now - timedelta(
                hours=DATA_VALIDITY_HOURS
            ):
                context = self.__get_location_objects_from_database(location)
            else:
                context = self.__get_all_weather_data(city)
        if context:
            return JsonResponse(context, safe=False)

    def __get_all_weather_data(self, city):
        forecast = WeatherApiAdapter().get_forecast(city)
        location, _ = Location.objects.get_or_create(**forecast["location"])
        now = datetime.now()
        CurrentWeather.objects.update_or_create(defaults ={**forecast["current"]}, location=location)
        history_days = self.__get_history_daily_weather(city, now)
        forecast_days = forecast["forecast_daily"]
        daily = []
        daily.extend(history_days)
        daily.extend(forecast_days)
        for day in daily:
            DailyWeather.objects.create(**day, location=location)
        context = {
            "location": forecast["location"],
            "current": forecast["current"],
            "daily": daily,
        }
        return context

    @staticmethod
    def __get_history_daily_weather(
        city: str, now: datetime, past_day_count=HISTORY_MAX_DAYS
    ):
        history_days = []
        for i in range(past_day_count, 0, -1):
            past_day = (now - timedelta(i)).strftime("%Y-%m-%d")
            history = WeatherApiAdapter().get_history_day(city, past_day)
            history and history_days.append(history)
        return history_days

    @staticmethod
    def __get_location_objects_from_database(location):
        location_dict = LocationResponseSchema().dump(location)
        current_dict = CurrentWeatherSchema().dump(location.currentweather)
        daily_dict = DailyWeatherSchema(many=True).dump(location.dailyweather_set.all())
        return {"location": location_dict, "current": current_dict, "daily": daily_dict}
