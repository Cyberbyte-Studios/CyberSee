from django.shortcuts import render
from rest_framework import viewsets
from cybersee.metrics.serializers import MetricSerializer, ReadingSerializer
from cybersee.metrics.models import Metric, Reading


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
