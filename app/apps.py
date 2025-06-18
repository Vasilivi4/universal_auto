from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    verbose_name = "Ninja Taxi"

    def ready(self):
        import app.signals  # noqa: F401  # Import for side effects (


# Django signals)
