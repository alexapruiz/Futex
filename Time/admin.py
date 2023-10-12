from django.contrib import admin
from Futex.models import Time

class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome','estado', 'valor')

# Register your models here.
admin.site.register(Time,TimeAdmin)