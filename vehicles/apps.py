from django.apps import AppConfig
# vehicles/apps.py
from django.db import models
from django.db.models import DecimalField # type: ignore


class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vehicles'

def ready(self):
    import vehicles.signals  # noqa