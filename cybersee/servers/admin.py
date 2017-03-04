from django.contrib import admin
from cybersee.servers.models import Server, Game, ServerLog


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('name', 'game', 'owner')
    search_fields = ('name', 'game__name', 'owner__username', 'owner__email')
    list_filter = ('game__name', )

@admin.register(ServerLog)
class ServerLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'server', 'message', 'recorded')
    search_fields = ('message', )
    list_filter = ('server__name', 'recorded' )
