from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from cybersee.payments.serializers import PlanSerializer
from cybersee.payments.models import Plan, Subscription
from cybersee.payments.providers import provider_braintree


class PlanView(LoginRequiredMixin, ListView):
    model = Plan
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.filter(hidden=False, enabled=True, price__gt=0.0)


class SubscribeView(LoginRequiredMixin, DetailView):
    template_name = 'payments/subscribe.html'
    model = Plan

    def customer(self):
        return provider_braintree.get_customer(self.request.user)

    def scripts(self):
        return provider_braintree.template_scripts()

    def get(self, request, **kwargs):
        if self.get_object().price == 0.0:
            messages.warning(request, 'You cannot buy a free plan')
            return redirect('plans-list')

        if Subscription.objects.filter(user=request.user, active=True).count() > 0:
            messages.warning(request, 'You already own this plan')
            return redirect('plans-list')
        return super(SubscribeView, self).get(request, **kwargs)

    def post(self, request, **kwargs):
        if provider_braintree.subscribe(self.get_object(), request):
            return redirect('dashboard')
        return super(SubscribeView, self).get(request, **kwargs)


class SubscriptionsView(LoginRequiredMixin, ListView):
    model = Subscription
    context_object_name = 'subscriptions'

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class PlanViewSet(viewsets.ModelViewSet):
    """
    list:
    View the plans which we have available.
    """
    queryset = Plan.objects.filter(hidden=False, enabled=True)
    serializer_class = PlanSerializer
    search_fields = ('name', 'description', 'retention')
    filter_fields = ('name', )
    ordering_fields = ('name', )
