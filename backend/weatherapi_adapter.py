import logging

from marshmallow import Schema, fields, pre_load, ValidationError

log = logging.getLogger(__name__)


class LocationSchema(Schema):
    name = fields.String(required=True)
    country = fields.String(required=False)
    latitude = fields.Float(required=True, load_from="lat")
    longitude = fields.Float(required=True, load_from="lon")
    timezone = fields.String(required=True, load_from="tz_id")


class CurrentWeatherSchema(Schema):
    time_epoch = fields.Integer(required=True, load_from="last_updated_epoch")
    temp_c = fields.Float(required=True)
    wind_kph = fields.Float(required=False)
    wind_dir = fields.String(required=False)
    pressure_mb = fields.Integer(required=False)
    precip_mm = fields.Integer(required=True)
    humidity = fields.Integer(required=False)
    condition = fields.String(required=True)

    @pre_load
    def get_condition(self, data):
        data["condition"] = data["condition"]["text"]
        return data


class DailyWeatherSchema(Schema):
    time_epoch = fields.Integer(required=True)
    maxtemp_c = fields.Float(required=True)
    mintemp_c = fields.Float(required=True)
    avgtemp_c = fields.Float(required=False)
    maxwind_kph = fields.Float(required=False)
    totalprecip_mm = fields.Integer(required=True)
    avghumidity = fields.Integer(required=False)
    condition = fields.String(required=True)

    @pre_load
    def get_condition(self, data):
        data["condition"] = data["condition"]["text"]
        return data


def prepare_location_object(location_data: dict):
    try:
        return LocationSchema().load(location_data).data
    except ValidationError as error:
        log.error(error)


def prepare_current_object(current_data: dict):
    try:
        return CurrentWeatherSchema().load(current_data).data
    except ValidationError as error:
        log.error(error)


def prepare_daily_object(daily_data: dict):
    daily_data["day"]["time_epoch"] = daily_data["date_epoch"]
    try:
        return DailyWeatherSchema().load(daily_data).data
    except ValidationError as error:
        log.error(error)
