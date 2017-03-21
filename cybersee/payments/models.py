from django.db import models
from cybersee.metrics.models import Metric
from cybersee.users.models import User


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    braintree_id = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    metrics = models.ManyToManyField(Metric)
    retention = models.IntegerField()
    hidden = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    user = models.ForeignKey(User)
    braintree_id = models.CharField(max_length=100)
    active = models.BooleanField(default=False)

    def __str__(self):
        return '{user} - {braintree}'.format(user=self.user, braintree=self.braintree_id)
