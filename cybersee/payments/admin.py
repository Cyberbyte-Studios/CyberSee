from django.contrib import admin
from cybersee.payments.models import Plan

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'retention', 'hidden', 'enabled')
    search_fields = ('name', 'price', 'retention')
    list_filter = ('retention', 'hidden', 'enabled')
