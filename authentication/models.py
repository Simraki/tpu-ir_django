from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, **extra_fields):
        if not email:
            raise ValueError('user must have email address')
        user = self.model(
            email=email,
            is_staff=is_staff,
            **extra_fields
        )

        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, **extra_fields)


class UserType(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'UserTypes'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=300)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'Users'
