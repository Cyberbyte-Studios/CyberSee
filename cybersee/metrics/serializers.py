from rest_framework import serializers
from cybersee.metrics.models import Metric, Reading


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = ('name', 'description', 'unit')

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('metric', 'value', 'recorded')
