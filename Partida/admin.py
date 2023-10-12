from django.contrib import admin
from Futex.models import Partida

class PartidaAdmin(admin.ModelAdmin):
    list_display = ('id_partida','id_rodada', 'id_time_casa' , 'id_time_visitante' , 'placar_time_casa' , 'placar_time_visitante')

# Register your models here.
admin.site.register(Partida,PartidaAdmin)