from datetime import datetime
from unittest.mock import patch

from django.test import Client, TestCase

from backend.test_data.api_data import (
    BUNDLED_5_DAYS_HISTORY_DATA,
    CURRENT_AND_FORECAST_FROM_API_2_DAYS,
)
from backend.weatherapi_adapter import WeatherApiAdapter


EXPECTED_WEATHER_DATA = {
    "location": {
        "name": "Bialystok",
        "country": "Poland",
        "latitude": 53.13,
        "longitude": 23.08,
        "timezone": "Europe/Warsaw",
    },
    "current": {
        "time_epoch": 1685268900,
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
            "date_epoch": 1684800000,  #  current minus 5 days
            "maxtemp_c": 20.6,
            "mintemp_c": 11.4,
            "avgtemp_c": 15.7,
            "maxwind_kph": 13.7,
            "totalprecip_mm": 0,
            "avghumidity": 64,
            "condition": "//static/sunny.png",
        },
        {
            "date_epoch": 1684886400,  #  current minus 4 days
            "maxtemp_c": 21.6,
            "mintemp_c": 12.4,
            "avgtemp_c": 16.7,
            "maxwind_kph": 14.7,
            "totalprecip_mm": 1,
            "avghumidity": 65,
            "condition": "//static/partly_cloudy.png",
        },
        {
            "date_epoch": 1684972800,  #  current minus 3 days
            "maxtemp_c": 22.6,
            "mintemp_c": 13.4,
            "avgtemp_c": 14.7,
            "maxwind_kph": 15.7,
            "totalprecip_mm": 5,
            "avghumidity": 56,
            "condition": "//static/partly_sunny.png",
        },
        {
            "date_epoch": 1685059200,  #  current minus 2 days
            "maxtemp_c": 19.6,
            "mintemp_c": 10.4,
            "avgtemp_c": 13.7,
            "maxwind_kph": 9.7,
            "totalprecip_mm": 0,
            "avghumidity": 52,
            "condition": "//static/overcast.png",
        },
        {
            "date_epoch": 1685145600,  # current minus 1 day
            "maxtemp_c": 18.6,
            "mintemp_c": 9.4,
            "avgtemp_c": 11.7,
            "maxwind_kph": 8.7,
            "totalprecip_mm": 6,
            "avghumidity": 51,
            "condition": "//static/clear.png",
        },
        {
            "date_epoch": 1685232000,  # current day
            "maxtemp_c": 17.6,
            "mintemp_c": 7.4,
            "avgtemp_c": 10.7,
            "maxwind_kph": 4.7,
            "totalprecip_mm": 2,
            "avghumidity": 50,
            "condition": "//static/cloudy.png",
        },
        {
            "date_epoch": 1685318400,  # current plus 1 day
            "maxtemp_c": 21.6,
            "mintemp_c": 12.4,
            "avgtemp_c": 15.7,
            "maxwind_kph": 10.7,
            "totalprecip_mm": 4,
            "avghumidity": 55,
            "condition": "//static/partly_sunny.png",
        },
        {
            "date_epoch": 1685404800,  # current plus 2 days
            "maxtemp_c": 21.6,
            "mintemp_c": 12.4,
            "avgtemp_c": 15.7,
            "maxwind_kph": 10.7,
            "totalprecip_mm": 4,
            "avghumidity": 55,
            "condition": "//static/partly_sunny.png",
        },
    ],
}


class TestMainView(TestCase):
    def setUp(self):
        self.client = Client()
        self.current_time = datetime(2023, 5, 27, 17, 15, 00, 000000)

    @patch.object(WeatherApiAdapter, "get_history_day")
    @patch.object(WeatherApiAdapter, "get_data_from_api")
    @patch("backend.views.datetime")
    def test_response_for_new_location_has_json_with_all_data(
        self, mock_date, get_forecast, get_history
    ):
        city = "bialystok"
        url = f"/main/{city}"
        get_forecast.return_value = CURRENT_AND_FORECAST_FROM_API_2_DAYS
        get_history.return_value = BUNDLED_5_DAYS_HISTORY_DATA
        mock_date.now.return_value = self.current_time

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        breakpoint()
        self.assertEqual(response.json(), EXPECTED_WEATHER_DATA)
