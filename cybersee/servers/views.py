from django.shortcuts import render
from rest_framework import viewsets
from cybersee.servers.serializers import ServerSerializer
from cybersee.servers.models import Server


class ServerViewSet(viewsets.ModelViewSet):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    search_fields = ('name', 'description')
    filter_fields = ('name', )
    ordering_fields = ('name', )
