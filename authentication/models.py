from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from authentication.managers import UserManager


class UserType(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'UserTypes'


class User(AbstractBaseUser):
    login = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    id_user_type = models.ForeignKey(UserType, models.DO_NOTHING, db_column='id_userType')
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'Users'
