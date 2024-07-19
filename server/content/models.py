from django.db import models
from django.contrib import admin

admin.register('root', admin)
class Country(models.Model):
    name = models.CharField(max_length=50)