from django.contrib import admin
from cybersee.metrics.models import Metric, Reading

@admin.register(Metric)
class MetricAdmin(admin.ModelAdmin):
    pass

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    pass
