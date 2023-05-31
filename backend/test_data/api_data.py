from weather.settings import API_KEY

CURRENT_AND_FORECAST_FROM_API_2_DAYS = {
    "location": {
        "name": "Bialystok",
        "region": "",
        "country": "Poland",
        "lat": 53.13,
        "lon": 23.08,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1685200637,
        "localtime": "2023-05-27 17:17",
    },
    "current": {
        "last_updated_epoch": 1685268900,
        "last_updated": "2023-05-27 17:15",
        "temp_c": 13.2,
        "temp_f": 58.8,
        "is_day": 1,
        "condition": {
            "text": "Partly Cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
            "code": 1000,
        },
        "wind_mph": 10.5,
        "wind_kph": 21.6,
        "wind_degree": 22,
        "wind_dir": "NNE",
        "pressure_mb": 1027,
        "pressure_in": 30.28,
        "precip_mm": 0,
        "precip_in": 0,
        "humidity": 37,
        "cloud": 9,
        "feelslike_c": 13.8,
        "feelslike_f": 56.8,
        "vis_km": 10,
        "vis_miles": 6,
        "uv": 4,
        "gust_mph": 13.9,
        "gust_kph": 22.3,
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2023-05-27",
                "date_epoch": 1685145600,
                "day": {
                    "maxtemp_c": 17.3,
                    "maxtemp_f": 63.1,
                    "mintemp_c": 4.9,
                    "mintemp_f": 40.8,
                    "avgtemp_c": 11.3,
                    "avgtemp_f": 52.3,
                    "maxwind_mph": 13.9,
                    "maxwind_kph": 22.3,
                    "totalprecip_mm": 0,
                    "totalprecip_in": 0,
                    "totalsnow_cm": 0,
                    "avgvis_km": 10,
                    "avgvis_miles": 6,
                    "avghumidity": 59,
                    "daily_will_it_rain": 0,
                    "daily_chance_of_rain": 0,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
                        "code": 1000,
                    },
                    "uv": 4,
                },
                "astro": {},
                "hour": [],
            },
            {
                "date": "2023-05-28",
                "date_epoch": 1685232000,
                "day": {
                    "maxtemp_c": 21.9,
                    "maxtemp_f": 71.4,
                    "mintemp_c": 5.5,
                    "mintemp_f": 41.9,
                    "avgtemp_c": 13.8,
                    "avgtemp_f": 56.9,
                    "maxwind_mph": 5.6,
                    "maxwind_kph": 9,
                    "totalprecip_mm": 0,
                    "totalprecip_in": 0,
                    "totalsnow_cm": 0,
                    "avgvis_km": 10,
                    "avgvis_miles": 6,
                    "avghumidity": 56,
                    "daily_will_it_rain": 0,
                    "daily_chance_of_rain": 0,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
                        "code": 1000,
                    },
                    "uv": 4,
                },
                "astro": {},
                "hour": [],
            },
            {
                "date": "2023-05-29",
                "date_epoch": 1685318400,
                "day": {
                    "maxtemp_c": 21.2,
                    "maxtemp_f": 70.2,
                    "mintemp_c": 8.1,
                    "mintemp_f": 46.6,
                    "avgtemp_c": 15.5,
                    "avgtemp_f": 59.9,
                    "maxwind_mph": 5.8,
                    "maxwind_kph": 9.4,
                    "totalprecip_mm": 0,
                    "totalprecip_in": 0,
                    "totalsnow_cm": 0,
                    "avgvis_km": 10,
                    "avgvis_miles": 6,
                    "avghumidity": 62,
                    "daily_will_it_rain": 0,
                    "daily_chance_of_rain": 0,
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": 0,
                    "condition": {
                        "text": "Partly cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                        "code": 1003,
                    },
                    "uv": 5,
                },
                "astro": {},
                "hour": [],
            },
        ]
    },
}

HISTORY_FROM_API_DAY_5 = {
    "location": {
        "name": "Bialystok",
        "region": "",
        "country": "Poland",
        "lat": 53.13,
        "lon": 23.08,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1685200350,
        "localtime": "2023-05-27 17:12",
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2023-05-22",
                "date_epoch": 1684713600,
                "day": {
                    "maxtemp_c": 19.5,
                    "maxtemp_f": 67.1,
                    "mintemp_c": 12.4,
                    "mintemp_f": 54.3,
                    "avgtemp_c": 15.4,
                    "avgtemp_f": 59.8,
                    "maxwind_mph": 4.9,
                    "maxwind_kph": 7.9,
                    "totalprecip_mm": 0,
                    "totalprecip_in": 0,
                    "avgvis_km": 10,
                    "avgvis_miles": 6,
                    "avghumidity": 63,
                    "condition": {
                        "text": "Partly cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                        "code": 1003,
                    },
                    "uv": 5,
                },
                "astro": {},
                "hour": [],
            }
        ]
    },
}

HISTORY_FROM_API_DAY_4 = {
    "location": {
        "name": "Bialystok",
        "region": "",
        "country": "Poland",
        "lat": 53.13,
        "lon": 23.08,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1685198070,
        "localtime": "2023-05-27 16:34",
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2023-05-23",
                "date_epoch": 1684800000,
                "day": {
                    "maxtemp_c": 20.6,
                    "maxtemp_f": 69.1,
                    "mintemp_c": 11.4,
                    "mintemp_f": 52.5,
                    "avgtemp_c": 15.7,
                    "avgtemp_f": 60.3,
                    "maxwind_mph": 8.5,
                    "maxwind_kph": 13.7,
                    "totalprecip_mm": 0,
                    "totalprecip_in": 0,
                    "avgvis_km": 10,
                    "avgvis_miles": 6,
                    "avghumidity": 64,
                    "condition": {
                        "text": "Partly cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                        "code": 1003,
                    },
                    "uv": 6,
                },
                "astro": {},
                "hour": [],
            }
        ]
    },
}

HISTORY_FROM_API_DAY_3 = {
    "location": {
        "name": "Bialystok",
        "region": "",
        "country": "Poland",
        "lat": 53.13,
        "lon": 23.08,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1685200082,
        "localtime": "2023-05-27 17:08",
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2023-05-24",
                "date_epoch": 1684886400,
                "day": {
                    "maxtemp_c": 21.9,
                    "maxtemp_f": 71.4,
                    "mintemp_c": 12.9,
                    "mintemp_f": 55.2,
                    "avgtemp_c": 16.7,
                    "avgtemp_f": 62.1,
                    "maxwind_mph": 8.1,
                    "maxwind_kph": 13,
                    "totalprecip_mm": 0,
                    "totalprecip_in": 0,
                    "avgvis_km": 10,
                    "avgvis_miles": 6,
                    "avghumidity": 60,
                    "condition": {
                        "text": "Partly cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                        "code": 1003,
                    },
                    "uv": 6,
                },
                "astro": {},
                "hour": [],
            }
        ]
    },
}

HISTORY_FROM_API_DAY_2 = {
    "location": {
        "name": "Bialystok",
        "region": "",
        "country": "Poland",
        "lat": 53.13,
        "lon": 23.08,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1685200158,
        "localtime": "2023-05-27 17:09",
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2023-05-25",
                "date_epoch": 1684972800,
                "day": {
                    "maxtemp_c": 22.6,
                    "maxtemp_f": 72.7,
                    "mintemp_c": 13.6,
                    "mintemp_f": 56.5,
                    "avgtemp_c": 17.7,
                    "avgtemp_f": 63.8,
                    "maxwind_mph": 6.5,
                    "maxwind_kph": 10.4,
                    "totalprecip_mm": 1.3,
                    "totalprecip_in": 0.05,
                    "avgvis_km": 9.2,
                    "avgvis_miles": 5,
                    "avghumidity": 69,
                    "condition": {
                        "text": "Patchy rain possible",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                        "code": 1063,
                    },
                    "uv": 5,
                },
                "astro": {},
                "hour": [],
            }
        ]
    },
}

HISTORY_FROM_API_DAY_1 = {
    "location": {
        "name": "Bialystok",
        "region": "",
        "country": "Poland",
        "lat": 53.13,
        "lon": 23.08,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1685200257,
        "localtime": "2023-05-27 17:10",
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2023-05-26",
                "date_epoch": 1685059200,
                "day": {
                    "maxtemp_c": 22.5,
                    "maxtemp_f": 72.5,
                    "mintemp_c": 7.6,
                    "mintemp_f": 45.7,
                    "avgtemp_c": 14.9,
                    "avgtemp_f": 58.8,
                    "maxwind_mph": 13.4,
                    "maxwind_kph": 21.6,
                    "totalprecip_mm": 0.2,
                    "totalprecip_in": 0.01,
                    "avgvis_km": 8.6,
                    "avgvis_miles": 5,
                    "avghumidity": 73,
                    "condition": {
                        "text": "Overcast",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/176.png",
                        "code": 1063,
                    },
                    "uv": 5,
                },
                "astro": {},
                "hour": [],
            }
        ]
    },
}

BUNDLED_DAILY_DATA_FROM_API = {
    f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q=bialystok&days=3": CURRENT_AND_FORECAST_FROM_API_2_DAYS,
    f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q=bialystok&dt=2023-05-26": HISTORY_FROM_API_DAY_1,
    f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q=bialystok&dt=2023-05-25": HISTORY_FROM_API_DAY_2,
    f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q=bialystok&dt=2023-05-24": HISTORY_FROM_API_DAY_3,
    f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q=bialystok&dt=2023-05-23": HISTORY_FROM_API_DAY_4,
    f"https://api.weatherapi.com/v1/history.json?key={API_KEY}&q=bialystok&dt=2023-05-22": HISTORY_FROM_API_DAY_5,
}


def return_history_day(url):
    return BUNDLED_DAILY_DATA_FROM_API[url]
