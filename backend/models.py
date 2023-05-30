from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timezone = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} / {self.country}"


class CurrentWeather(models.Model):
    last_updated = models.DateTimeField()
    temp_c = models.FloatField()
    wind_kph = models.FloatField()
    wind_dir = models.CharField(max_length=3)
    pressure_mb = models.IntegerField()
    precip_mm = models.IntegerField()
    humidity = models.IntegerField()
    condition = models.CharField(max_length=256)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)


class DailyWeather(models.Model):
    date = models.DateField()
    maxtemp_c = models.FloatField()
    mintemp_c = models.FloatField()
    avgtemp_c = models.FloatField()
    maxwind_kph = models.FloatField()
    totalprecip_mm = models.FloatField()
    avghumidity = models.IntegerField()
    condition = models.CharField(max_length=256)
    location = models.ForeignKey(Location, null=False, on_delete=models.CASCADE)
