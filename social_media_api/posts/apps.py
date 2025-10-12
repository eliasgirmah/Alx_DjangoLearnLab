from django.apps import AppConfig
def ready(self):
    import posts.signals  # for posts app


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
