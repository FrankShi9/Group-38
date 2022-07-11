from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserInfo(models.Model):
    email = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=64)


class UserFile(models.Model):
    userEmail = models.ForeignKey(UserInfo, on_delete=models.CASCADE,to_field='email')
    fileName = models.CharField(max_length=32)
    fileDescription = models.CharField(max_length=200, null=True)
    uploadDate = models.DateTimeField(default=timezone.now, blank=True)


class UserLog(models.Model):
    userEmail = models.ForeignKey(UserInfo, on_delete=models.CASCADE, to_field='email')
    fileName = models.CharField(max_length=32)
    actionDescription = models.CharField(max_length=200, null=True)
    actionDate = models.DateTimeField(default=timezone.now, blank=True)
    reportName = models.CharField(max_length=32, null=True)

