from django.urls import path
from .views import *


app_name = 'gerencia'


urlpatterns = [
    path('scores-jogador/<int:id>/', JogadorScores, name='detail_score'),
    path('graficos/<int:id>/', grafico, name='grafic_jogador'),
    path('new-score', login_required(CreateScore.as_view()), name='new_score'),
    path('new-especifico', login_required(CreateEspecifico.as_view()), name='new_especifico'),
    path('detail-especifico/<int:pk>/', login_required(DetailEspecifico.as_view()), name='detail_especifico'),
]
