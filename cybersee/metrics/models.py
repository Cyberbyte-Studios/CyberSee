from django.db import models
from django.utils import timezone

class Metric(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=5)

class Reading(models.Model):
    metric = models.ForeignKey(Metric)
    value = models.FloatField()#TODO:
    recorded = models.DateTimeField(default=timezone.now, db_index=True)
