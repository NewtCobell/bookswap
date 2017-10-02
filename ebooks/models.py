from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    deleted = models.BooleanField()
    added_on = models.DateTimeField()
    available_date = models.DateField()

