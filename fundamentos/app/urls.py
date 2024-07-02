from django.urls import path
from .views import horario_atual

urlpatterns = [
    path('horario_atual',horario_atual)
]
