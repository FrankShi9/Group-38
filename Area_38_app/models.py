from django.db import models
from django.contrib.auth.models import User

user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)