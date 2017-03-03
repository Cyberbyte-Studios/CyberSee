import uuid
from django.db import models
from cybersee.metrics.models import Metric
from cybersee.users.models import Community

class Server(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    metrics = models.ManyToManyField(Metric)
    community = models.OneToOneField(Community)

    def __str__(self):
        return self.name
