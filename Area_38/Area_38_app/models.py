from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=64)