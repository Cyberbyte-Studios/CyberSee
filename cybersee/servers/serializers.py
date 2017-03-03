from rest_framework import serializers
from cybersee.servers.models import Server


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = ('name', 'description', 'metrics')
        
