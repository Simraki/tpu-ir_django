from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, login, password, is_staff, **extra_fields):
        if not login:
            raise ValueError('user must have login address')
        user = self.model(
            login=login,
            is_staff=is_staff,
            **extra_fields
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, password=None, **extra_fields):
        return self._create_user(login, password, False, **extra_fields)

    def create_superuser(self, login, password=None, **extra_fields):
        return self._create_user(login, password, True, **extra_fields)
