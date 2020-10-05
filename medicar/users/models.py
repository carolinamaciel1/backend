from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class UsuarioCustomizado(AbstractBaseUser):
    username = None
    email = models.EmailField(unique=True)
    name = models.CharField(null=False, blank=False, max_length=128)
    password = models.CharField(max_length=128)
    re_password = models.CharField(max_length=128)
    USERNAME_FIELD = 'email'
