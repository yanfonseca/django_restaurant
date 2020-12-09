from django.db import models
from datetime import datetime
# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredient = models.TextField()
    preparation = models.TextField()
    preparation_time = models.IntegerField()
    portions = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.now, blank=True)


