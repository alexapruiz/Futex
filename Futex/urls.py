from django.contrib import admin
from django.urls import path , include
from Futex import views

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.dashboard),
    path('', views.dashboard),
    path('admin/', admin.site.urls),
    path('carteira/', include('Carteira.urls')),
    path('time/', include('Time.urls')),
    path('atualiza_acoes/', include('Atualiza_Acoes.urls')),
    path('tabela_jogos/<str:tipo_filtro>/', views.tabela_jogos),
    path('perfil_usuario/', views.perfil_usuario),
    path('perfil_usuario/atualiza', views.atualiza_usuario),
    ]
