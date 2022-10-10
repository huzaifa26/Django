from unittest.util import _MAX_LENGTH
from django.db import models

class Drink(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=500)