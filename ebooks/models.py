from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    deleted = models.BooleanField()
    added_on = models.DateTimeField()
    available_date = models.DateField()
