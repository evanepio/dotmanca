from django.apps import AppConfig


class GalleryConfig(AppConfig):
    name = "gallery"

    def ready(self):
        # Only need to import them because the decorators will register on load
        from .signals import handlers
