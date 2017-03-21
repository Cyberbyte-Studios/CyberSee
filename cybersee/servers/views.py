from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import viewsets

from cybersee.base.helpers import get_user_or_none
from cybersee.servers.serializers import ServerSerializer, GameSerializer, ServerLogSerializer
from cybersee.servers.models import Server, Game, ServerLog
from cybersee.servers.tables import ServerLogTable


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    search_fields = ('game__name', 'name')
    filter_fields = ('owner', 'name')

    def get_queryset(self):
        return Server.objects.filter(owner=get_user_or_none(self.request))


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    search_fields = ('name', 'description')
    filter_fields = ('name', )
    ordering_fields = ('name', )


class ServerLogViewSet(viewsets.ModelViewSet):
    queryset = ServerLog.objects.all()
    serializer_class = ServerLogSerializer
    search_fields = ('server__name', 'message')
    filter_fields = ('server', 'recorded')
    ordering_fields = ('server', 'recorded')

    def get_queryset(self):
        return ServerLog.objects.filter(server__owner=get_user_or_none(self.request))


class ServerView(LoginRequiredMixin, DetailView):
    model = Server

    def get_context_data(self, **kwargs):
        context = super(ServerView, self).get_context_data(**kwargs)
        context['server_log_table'] = ServerLogTable(ServerLog.objects.filter(server=self.object))
        return context

class NewServerView(LoginRequiredMixin, CreateView):
    model = Server
    template_name = "servers/add_server.html"
    fields = ['name', 'description', 'game']

    def form_valid(self, form):
            form.instance.owner = self.request.user
            return super(NewServerView, self).form_valid(form)

class EditServerView(LoginRequiredMixin, UpdateView):
    model = Server
    template_name = "servers/edit_server.html"
    fields = ['name', 'description', 'game']

    def form_valid(self, form):
            form.instance.owner = self.request.user
            return super(EditServerView, self).form_valid(form)
