from rest_framework import serializers
from cybersee.servers.models import Server, Game, ServerLog


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('pk', 'name', 'description')


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('pk', 'name', 'owner', 'description', 'game')


class ServerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerLog
        fields = ('pk', 'server', 'message', 'recorded')
