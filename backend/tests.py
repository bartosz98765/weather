from datetime import datetime
from unittest.mock import patch

from django.test import Client, TestCase

from backend.models import Location
from backend.test_data.api_data import (
    BUNDLED_DAILY_DATA_FROM_API,
    CURRENT_AND_FORECAST_FROM_API_2_DAYS,
    return_history_day,
)
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
        assert location.name == EXPECTED_WEATHER_DATA["location"]["name"]
        assert location.country == EXPECTED_WEATHER_DATA["location"]["country"]
        assert location.latitude == EXPECTED_WEATHER_DATA["location"]["latitude"]
        assert location.longitude == EXPECTED_WEATHER_DATA["location"]["longitude"]
        assert location.timezone == EXPECTED_WEATHER_DATA["location"]["timezone"]
