from django.apps import AppConfig


class OilappConfig(AppConfig):
    name = 'oilapp'

    def ready(self):
        import oilapp.signals