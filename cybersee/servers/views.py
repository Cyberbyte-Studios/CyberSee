from django.shortcuts import render
from rest_framework import viewsets
from cybersee.servers.serializers import ServerSerializer, GameSerializer, ServerLogSerializer
from cybersee.servers.models import Server, Game, ServerLog


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    search_fields = ('name', 'description')
    filter_fields = ('name', )
    ordering_fields = ('name', )

    def get_queryset(self):
        user = self.request.user
        return Server.objects.filter(owner=user)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    search_fields = ('name', 'description')
    filter_fields = ('name', )
    ordering_fields = ('name', )

class ServerLogViewSet(viewsets.ModelViewSet):
    queryset = ServerLog.objects.all()
    serializer_class = ServerLogSerializer
    search_fields = ('name', 'description')
    filter_fields = ('name', )
    ordering_fields = ('name', )

    def get_queryset(self):
        user = self.request.user
        return ServerLog.objects.filter(server__owner=user)
