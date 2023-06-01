from datetime import datetime, timedelta
from unittest.mock import patch

from django.forms import model_to_dict
from django.test import Client, TestCase

from backend.models import Location, CurrentWeather, DailyWeather
from backend.test_data.api_data import return_history_day
from backend.weatherapi_adapter import WeatherApiAdapter

EXPECTED_WEATHER_DATA = {
    "location": {
        "name": "bialystok",
        "country": "Poland",
        "latitude": 53.13,
        "longitude": 23.08,
        "timezone": "Europe/Warsaw",
    },
    "current": {
        "last_updated": "2023-05-27T17:15:00",
        "temp_c": 13.2,
        "wind_kph": 21.6,
        "wind_dir": "NNE",
        "pressure_mb": 1027,
        "precip_mm": 0,
        "humidity": 37,
        "condition": "//static/partly-cloudy.png",
    },
    "daily": [
        {
            "date": "2023-05-22",  # current minus 5 days
            "maxtemp_c": 19.5,
            "mintemp_c": 12.4,
            "avgtemp_c": 15.4,
            "maxwind_kph": 7.9,
            "totalprecip_mm": 0.0,
            "avghumidity": 63,
            "condition": "//static/partly-cloudy.png",
        },
        {
            "date": "2023-05-23",  #  current minus 4 days
            "maxtemp_c": 20.6,
            "mintemp_c": 11.4,
            "avgtemp_c": 15.7,
            "maxwind_kph": 13.7,
            "totalprecip_mm": 0.0,
            "avghumidity": 64,
            "condition": "//static/partly-cloudy.png",
        },
        {
            "date": "2023-05-24",  #  current minus 3 days
            "maxtemp_c": 21.9,
            "mintemp_c": 12.9,
            "avgtemp_c": 16.7,
            "maxwind_kph": 13.0,
            "totalprecip_mm": 0.0,
            "avghumidity": 60,
            "condition": "//static/partly-cloudy.png",
        },
        {
            "date": "2023-05-25",  #  current minus 2 days
            "maxtemp_c": 22.6,
            "mintemp_c": 13.6,
            "avgtemp_c": 17.7,
            "maxwind_kph": 10.4,
            "totalprecip_mm": 1.3,
            "avghumidity": 69,
            "condition": "//static/patchy-rain-possible.png",
        },
        {
            "date": "2023-05-26",  #  current minus 1 days
            "maxtemp_c": 22.5,
            "mintemp_c": 7.6,
            "avgtemp_c": 14.9,
            "maxwind_kph": 21.6,
            "totalprecip_mm": 0.2,
            "avghumidity": 73,
            "condition": "//static/overcast.png",
        },
        {
            "date": "2023-05-27",  # current day
            "maxtemp_c": 17.3,
            "mintemp_c": 4.9,
            "avgtemp_c": 11.3,
            "maxwind_kph": 22.3,
            "totalprecip_mm": 0.0,
            "avghumidity": 59,
            "condition": "//static/sunny.png",
        },
        {
            "date": "2023-05-28",  # current plus 1 day
            "maxtemp_c": 21.9,
            "mintemp_c": 5.5,
            "avgtemp_c": 13.8,
            "maxwind_kph": 9.0,
            "totalprecip_mm": 0.0,
            "avghumidity": 56,
            "condition": "//static/sunny.png",
        },
        {
            "date": "2023-05-29",  # current plus 2 day
            "maxtemp_c": 21.2,
            "mintemp_c": 8.1,
            "avgtemp_c": 15.5,
            "maxwind_kph": 9.4,
            "totalprecip_mm": 0.0,
            "avghumidity": 62,
            "condition": "//static/partly-cloudy.png",
        },
    ],
}


class TestMainView(TestCase):
    def setUp(self):
        self.client = Client()
        self.current_time = datetime(2023, 5, 27, 17, 15, 00, 000000)

    @patch.object(WeatherApiAdapter, "get_data_from_api")
    @patch("backend.views.datetime")
    def test_response_for_new_location_has_json_with_all_data(
        self, mock_date, get_data_from_api
    ):
        city = "bialystok"
        url = f"/main/{city}"
        get_data_from_api.side_effect = return_history_day
        mock_date.now.return_value = self.current_time

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), EXPECTED_WEATHER_DATA)

    @patch.object(WeatherApiAdapter, "get_data_from_api")
    @patch("backend.views.datetime")
    def test_saving_new_location_weather_data(self, mock_date, get_data_from_api):
        city = "bialystok"
        url = f"/main/{city}"
        get_data_from_api.side_effect = return_history_day
        mock_date.now.return_value = self.current_time

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        location = Location.objects.get(name=city)
        location_dict = model_to_dict(
            location, fields=["name", "country", "latitude", "longitude", "timezone"]
        )
        assert location_dict == EXPECTED_WEATHER_DATA["location"]

        current_weather = CurrentWeather.objects.get(location=location)
        current_weather_dict = model_to_dict(
            current_weather,
            fields=[
                "last_updated",
                "temp_c",
                "wind_kph",
                "wind_dir",
                "pressure_mb",
                "precip_mm",
                "humidity",
                "condition",
            ],
        )
        expected_last_updated_iso = EXPECTED_WEATHER_DATA["current"].pop("last_updated")
        last_updated = current_weather_dict.pop("last_updated")
        last_updated_iso = last_updated.isoformat()
        assert last_updated_iso.replace("+00:00", "") == expected_last_updated_iso
        assert current_weather_dict == EXPECTED_WEATHER_DATA["current"]

        daily_weather = DailyWeather.objects.filter(location=location)
        assert len(daily_weather) == len(EXPECTED_WEATHER_DATA["daily"])

        history_5_day = daily_weather.filter(date=self.current_time - timedelta(days=5)).first()
        history_5_day_dict = model_to_dict(
            history_5_day,
            fields=[
                "date",
                "maxtemp_c",
                "mintemp_c",
                "avgtemp_c",
                "maxwind_kph",
                "totalprecip_mm",
                "avghumidity",
                "condition",
            ],
        )

        expected_date_iso = EXPECTED_WEATHER_DATA["daily"][0].pop("date")
        date = history_5_day_dict.pop("date")
        date_iso = date.isoformat()
        assert date_iso.replace("+00:00", "") == expected_date_iso
        assert history_5_day_dict == EXPECTED_WEATHER_DATA["daily"][0]
