from authentication.models import User


def authenticate(login=None, password=None, **kwargs):
    try:
        user = User.objects.get(login=login)
        if user.check_password(password):
            return user
    except User.DoesNotExist:
        return None


class UserAuthBackend:
    pass
