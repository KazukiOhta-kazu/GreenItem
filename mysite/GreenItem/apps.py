from django.apps import AppConfig


class GreenitemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'greenitem'

    def ready(self):
        import greenitem.signals
