from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=128)
    date = models.DateField()
