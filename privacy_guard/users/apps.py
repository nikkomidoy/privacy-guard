from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "privacy_guard.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import privacy_guard.users.signals  # noqa: F401
        except ImportError:
            pass
