# Generated by Django 4.2.1 on 2023-05-28 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CurrentWeather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_epoch", models.IntegerField()),
                ("temp_c", models.FloatField()),
                ("wind_kph", models.FloatField()),
                ("wind_dir", models.CharField(max_length=3)),
                ("pressure_mb", models.IntegerField()),
                ("precip_mm", models.IntegerField()),
                ("humidity", models.IntegerField()),
                ("condition", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="DailyWeather",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_epoch", models.IntegerField()),
                ("maxtemp_c", models.FloatField()),
                ("mintemp_c", models.FloatField()),
                ("avgtemp_c", models.FloatField()),
                ("maxwind_kph", models.FloatField()),
                ("totalprecip_mm", models.IntegerField()),
                ("avghumidity", models.IntegerField()),
                ("condition", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("country", models.CharField(max_length=64)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                ("timezone", models.CharField(max_length=64)),
            ],
        ),
    ]