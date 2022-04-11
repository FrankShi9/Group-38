from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserInfo(models.Model):
    email = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)


class UserFile(models.Model):
    userEmail = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    file = models.FileField(upload_to='', null=True)
    fileDescription = models.CharField(max_length=200, null=True)
    uploadDate = models.DateTimeField(default=timezone.now, blank=True)
