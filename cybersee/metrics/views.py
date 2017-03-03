from django.shortcuts import render
from rest_framework import viewsets
from cybersee.metrics.serializers import MetricSerializer, ReadingSerializer
from cybersee.metrics.models import Metric, Reading


class MetricViewSet(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    search_fields = ('name', 'unit')
    filter_fields = ('name', 'unit')
    ordering_fields = ('name', 'unit')

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    search_fields = ('metric__name', )
    filter_fields = ('metric', 'value', 'recorded')
    ordering_fields = ('metric', 'value', 'recorded')
