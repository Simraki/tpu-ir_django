from django.utils import timezone
from django.contrib.auth.backends import ModelBackend

from authentication.models import User


class EmailAuthBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                user.last_login = timezone.now()
                user.save(update_fields=['last_login'])
                return user
        except User.DoesNotExist:
            return None
