# apps.py
from django.apps import AppConfig

class Cooking-ApiConfig(AppConfig):
    name = 'cooking_api'

    # Connect the signals
    def ready(self):
        import cooking_api.signals  # noqa
