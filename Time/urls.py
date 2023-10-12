from django.urls import path
from . import views

urlpatterns = [
    path('', views.consultar),
    path('criar', views.criar),
    path('edit/<int:id>/', views.editar),
    path('delete/<int:id>/', views.excluir),
]
