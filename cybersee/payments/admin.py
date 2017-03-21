from django.contrib import admin
from cybersee.payments.models import Plan, Subscription


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'retention', 'hidden', 'enabled')
    search_fields = ('name', 'price', 'retention')
    list_filter = ('retention', 'hidden', 'enabled')


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'braintree_id', 'active')
    search_fields = ('user__id', 'user__name', 'user__username', 'braintree_id')
    list_filter = ('active',)
