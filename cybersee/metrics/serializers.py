from rest_framework import serializers
from cybersee.metrics.models import Metric, Reading


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ('pk', 'name', 'description', 'unit')

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('pk', 'server', 'metric', 'value', 'recorded')
