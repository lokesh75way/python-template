from django.apps import AppConfig


class MainappConfig(AppConfig):
    name = 'mainapp'

    # 4.5 Middleware & Signals (Signals)
    def ready(self):
        import mainapp.signals
