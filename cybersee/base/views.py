from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from cybersee.servers.models import Server


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['servers'] = Server.objects.filter(owner=self.request.user)
        return context
