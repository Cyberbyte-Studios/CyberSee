from rest_framework import viewsets
from cybersee.payments.serializers import PlanSerializer
from cybersee.payments.models import Plan


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.filter(hidden=False, enabled=True)
    serializer_class = PlanSerializer
    search_fields = ('name', 'description', 'retention')
    filter_fields = ('name', )
    ordering_fields = ('name', )
