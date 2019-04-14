from django.apps import AppConfig


class MavrodiConfig(AppConfig):
    name = 'mavrodi'
    verbose_name = 'Мавроди'

    def ready(self):
        import mavrodi.signals
