from django.db import models
from datetime import datetime
# Create your models here.

from people.models import PeopleModel

class Recipe(models.Model):

    person = models.ForeignKey(
        PeopleModel, 
        on_delete=models.CASCADE,
        default='')

    name = models.CharField(max_length=200)
    ingredient = models.TextField()
    preparation = models.TextField()
    preparation_time = models.IntegerField()
    portions = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    created_at = models.DateField(default=datetime.now, blank=True)


