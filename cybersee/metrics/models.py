from django.db import models
from django.utils import timezone

from cybersee.servers.models import Server


class Metric(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    unit = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.name


class Reading(models.Model):
    metric = models.ForeignKey(Metric)
    value = models.FloatField()
    recorded = models.DateTimeField(default=timezone.now, db_index=True)
    server = models.ForeignKey(Server)

    def __str__(self):
        return self.metric.name

    class Meta:
        ordering = ['-recorded']
