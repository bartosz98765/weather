import logging
from dataclasses import dataclass
from datetime import timezone
from typing import List, Optional

import requests
from django.utils.text import slugify
from marshmallow import Schema, ValidationError, fields, post_load, pre_load
from requests import ConnectionError, Timeout

from weather.settings import API_KEY, FORECAST_DAYS_NO, WEATHER_API_ENDPOINT

log = logging.getLogger(__name__)


class LocationSchema(Schema):
    name = fields.String(required=True)
    country = fields.String(required=True)
    latitude = fields.Float(required=True, data_key="lat")
    longitude = fields.Float(required=True, data_key="lon")
    timezone = fields.String(required=True, data_key="tz_id")

    class Meta:
        ordered = True

    @pre_load
    def name_to_lower(self, data, many, partial):
        data["name"] = data["name"].lower()
        return data


class CurrentWeatherSchema(Schema):
    last_updated = fields.DateTime(required=True)
    temp_c = fields.Float(required=True)
    wind_kph = fields.Float(required=False)
    wind_dir = fields.String(required=False)
    pressure_mb = fields.Integer(required=False)
    precip_mm = fields.Integer(required=True)
    humidity = fields.Integer(required=False)
    condition = fields.String(required=True)

    class Meta:
        ordered = True

    @pre_load
    def get_condition(self, data, many, partial):
        data["condition"] = data["condition"]["text"]
        return data

    @post_load
    def modify_data(self, data, many, partial):
        data["last_updated"] = (
            data["last_updated"].replace(tzinfo=timezone.utc)
        ).isoformat()
        data["condition"] = make_condition_path(data["condition"])
        return data


class DailyWeatherSchema(Schema):
    date = fields.Date(required=True)
    maxtemp_c = fields.Float(required=True)
    mintemp_c = fields.Float(required=True)
    avgtemp_c = fields.Float(required=False)
    maxwind_kph = fields.Float(required=False)
    totalprecip_mm = fields.Float(required=True)
    avghumidity = fields.Integer(required=False)
    condition = fields.String(required=True)

    class Meta:
        ordered = True

    @pre_load
    def get_condition(self, data, many, partial):
        data["maxtemp_c"] = data["day"]["maxtemp_c"]
        data["mintemp_c"] = data["day"]["mintemp_c"]
        data["avgtemp_c"] = data["day"]["avgtemp_c"]
        data["maxwind_kph"] = data["day"]["maxwind_kph"]
        data["totalprecip_mm"] = data["day"]["totalprecip_mm"]
        data["avghumidity"] = data["day"]["avghumidity"]
        data["condition"] = data["day"]["condition"]["text"]
        return data

    @post_load
    def add_condition_path(self, data, many, partial):
        data["condition"] = make_condition_path(data["condition"])
        return data


def prepare_location_object(location_data: dict):
    try:
        return LocationSchema(unknown="exclude").load(location_data)
    except ValidationError as error:
        log.error(error)


def prepare_current_object(current_data: dict):
    try:
        return CurrentWeatherSchema(unknown="exclude").load(current_data)
    except ValidationError as error:
        log.error(error)


def prepare_daily_object(daily_data: dict) -> dict:
    try:
        return DailyWeatherSchema(unknown="exclude").load(daily_data)
    except ValidationError as error:
        log.error(error)


def prepare_daily_objects_list(daily_data: dict) -> List[dict]:
    try:
        return DailyWeatherSchema(unknown="exclude", many=True).load(daily_data)
    except ValidationError as error:
        log.error(error)


@dataclass(frozen=True)
class WeatherApiAdapter:
    endpoint: str = WEATHER_API_ENDPOINT

    def get_forecast(self, city: str) -> dict:
        url = f"{self.endpoint}forecast.json?key={API_KEY}&q={city}&days={FORECAST_DAYS_NO}"
        forecast = self.get_data_from_api(url)
        if forecast:
            return {
                "location": prepare_location_object(forecast["location"]),
                "current": prepare_current_object(forecast["current"]),
                "forecast_daily": prepare_daily_objects_list(
                    forecast["forecast"]["forecastday"]
                ),
            }

    def get_history_day(self, city: str, past_day) -> dict:
        url = f"{self.endpoint}history.json?key={API_KEY}&q={city}&dt={past_day}"
        history = self.get_data_from_api(url)
        if history:
            return prepare_daily_object(history["forecast"]["forecastday"][0])

    @staticmethod
    def get_data_from_api(url: str):
        try:
            response = requests.get(url, timeout=10)
        except (ConnectionError, Timeout) as error:
            log.error(error)
        else:
            return response.json()


def make_condition_path(condition):
    return f"//static/{slugify(condition).lower()}.png"
