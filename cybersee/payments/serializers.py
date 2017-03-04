from rest_framework import serializers
from cybersee.payments.models import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('name', 'price', 'retention', 'hidden', 'enabled')
