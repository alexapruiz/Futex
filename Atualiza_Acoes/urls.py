from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_atualiza_acoes),
    path('atualiza', views.atualiza_acoes),
    path('regras', views.regras),
]