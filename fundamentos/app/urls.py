from django.urls import path
from .views import horario_atual, exibir_templates

urlpatterns = [
    path('horario_atual/', horario_atual),
    path('cadastro_cliente/', exibir_templates,),]
