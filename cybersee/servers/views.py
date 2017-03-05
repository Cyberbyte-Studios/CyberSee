from rest_framework import viewsets

from cybersee.base.helpers import get_user_or_none
from cybersee.servers.serializers import ServerSerializer, GameSerializer, ServerLogSerializer
from cybersee.servers.models import Server, Game, ServerLog


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
