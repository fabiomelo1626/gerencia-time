from django.contrib import admin
from .models import *


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
        model = Jogador
        fields = ['nome', 'idade', 'posicao', 'posicao_opcao', 'cpf', 'lesoes', 'foto']
        list_display = ['nome', 'posicao', 'partidas', 'acerto_passe_curto', 'media_acert_pass_curt',
                        'media_pass_gol', 'media_faltas', 'media_gols', 'media_cart_amar',
                        'media_cart_verm']