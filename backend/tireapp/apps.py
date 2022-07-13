from django.apps import AppConfig


class TireappConfig(AppConfig):
    name = "tireapp"

    def ready(self):
        import tireapp.signals
