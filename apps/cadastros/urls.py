from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *


app_name = 'cadastros'


urlpatterns = [
    path('create-jogador', login_required(CreateJogador.as_view()), name='new_jogador'),
    path('list-jogador', login_required(ListJogador.as_view()), name='list_jogador'),
    path('detail-jogador/<int:pk>/', login_required(DetailJogador.as_view()), name='detail_jogador'),
]
