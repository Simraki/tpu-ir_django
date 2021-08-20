from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, **extra_fields):
        if not email:
            raise ValueError('User must have email address')
        if not password:
            raise ValueError('User must have password')

        user = self.model(email=email, is_staff=is_staff, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, is_staff=False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, is_staff=True, **extra_fields)
