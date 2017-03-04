from django.contrib import admin
from cybersee.metrics.models import Metric, Reading

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'unit')

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('id', 'server', 'metric', 'value', 'recorded')
    search_fields = ('id', 'server__name', 'metric__name')
    list_filter = ('server__name', 'metric', 'recorded')
