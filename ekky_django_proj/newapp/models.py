from re import M
from unicodedata import name
from django.db import models

# Create your models here.
class Schools(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)