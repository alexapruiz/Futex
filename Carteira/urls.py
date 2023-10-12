from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_carteira),
    path('vender/<int:id_time>/', views.vender_acao),
    path('comprar/<int:id_time>/', views.comprar_acao),
]