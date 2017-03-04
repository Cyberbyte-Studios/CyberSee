import uuid
from django.db import models
from cybersee.metrics.models import Metric
from cybersee.users.models import User
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    metrics = models.ManyToManyField(Metric)
    owner = models.ForeignKey(User)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name

class ServerLog(models.Model):
    server = models.ForeignKey(Server)
    message = models.TextField()
    recorded = models.DateTimeField(default=timezone.now, db_index=True)
