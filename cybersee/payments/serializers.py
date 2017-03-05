from rest_framework import serializers
from cybersee.payments.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('pk', 'name', 'price', 'retention', 'metrics', 'hidden', 'enabled')
