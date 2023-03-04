from django.apps import AppConfig


class NewsPortalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'News_Portal_app'

    def ready(self):
        import News_Portal_app.signals