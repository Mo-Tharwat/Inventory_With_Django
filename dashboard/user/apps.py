from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    #Step 13; Add the following method to using signals from user model
    def ready(self):
        from user import signals