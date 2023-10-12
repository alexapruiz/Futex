from django.contrib import admin
from Futex.models import Parametros

class ParametrosAdmin(admin.ModelAdmin):
    list_display = ('ID_PARAMETRO' , 'VITORIA_CASA','VITORIA_FORA', 'EMPATE_CASA' , 'EMPATE_FORA' , 'DERROTA_CASA' , 'DERROTA_FORA')

# Register your models here.
admin.site.register(Parametros,ParametrosAdmin)