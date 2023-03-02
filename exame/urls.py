from django.urls import path

from . import views

app_name = 'exame'

urlpatterns = [
    path('', views.index, name='index'),
    path('gerar_exame/', views.gerar_exame, name='gerar_exame'),
    path('acessar_exame/', views.acessar_exame, name='acessar_exame'),
    path('exame/', views.exame, name='exame'),
    path('exame/<cod_exame>', views.exame_via_link, name='exame_via_link'),
    path('gerando_exame/<exame>/<tema>', views.gerando_exame, name='gerando_exame'),
    
]