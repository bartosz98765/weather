# Generated by Django 4.2.1 on 2023-06-01 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
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
                ("name", models.CharField(max_length=64, unique=True)),
                ("country", models.CharField(blank=True, max_length=64, null=True)),
                ("latitude", models.FloatField(blank=True, null=True)),
                ("longitude", models.FloatField(blank=True, null=True)),
                ("timezone", models.CharField(blank=True, max_length=64, null=True)),
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
                ("date", models.DateField()),
                ("maxtemp_c", models.FloatField()),
                ("mintemp_c", models.FloatField()),
                ("avgtemp_c", models.FloatField()),
                ("maxwind_kph", models.FloatField()),
                ("totalprecip_mm", models.FloatField()),
                ("avghumidity", models.IntegerField()),
                ("condition", models.CharField(max_length=256)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.location",
                    ),
                ),
            ],
        ),
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
                ("last_updated", models.DateTimeField()),
                ("temp_c", models.FloatField()),
                ("wind_kph", models.FloatField()),
                ("wind_dir", models.CharField(max_length=3)),
                ("pressure_mb", models.IntegerField()),
                ("precip_mm", models.IntegerField()),
                ("humidity", models.IntegerField()),
                ("condition", models.CharField(max_length=256)),
                (
                    "location",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.location",
                    ),
                ),
            ],
        ),
    ]
