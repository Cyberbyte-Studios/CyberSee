from django.contrib import admin
from cybersee.servers.models import Server

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    pass
