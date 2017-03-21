import uuid
from django.db import models
from django.utils import timezone
from django.urls import reverse
from cybersee.users.models import User


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
    owner = models.ForeignKey(User)
    game = models.ForeignKey(Game)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('server-detail', kwargs={'pk': self.pk})

class ServerLog(models.Model):
    server = models.ForeignKey(Server)
    message = models.TextField()
    recorded = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        ordering = ['-recorded']

class ServerInfo(models.Model):
    operating_system = models.CharField(max_length=100, blank=True)
    cpu_model = models.CharField(max_length=100, blank=True)
    core_count = models.SmallIntegerField(blank=True)
    core_freq = models.FloatField(blank=True)
    max_mem = models.PositiveIntegerField(blank=True)
    game_version = models.CharField(max_length=100, blank=True)
    server = models.OneToOneField(Server)
