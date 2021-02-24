from django.urls import path
from .views import *


app_name = 'cadastros'


urlpatterns = [
    path('create-jogador', CreateJogador.as_view(), name='new_jogador')
]
