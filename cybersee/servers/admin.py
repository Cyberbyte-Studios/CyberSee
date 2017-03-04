from django.contrib import admin
from cybersee.servers.models import Server, Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'owner')
    search_fields = ('name', 'game__name', 'owner__name')
    list_filter = ('game__name', )
