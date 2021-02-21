from django.contrib import admin
from .models import *


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
        model = Jogador
        fields = ('nome', 'idade', 'posicao', 'posicao_opcao', 'cpf', 'lesoes', 'foto')
        list_display = ('nome', 'idade', 'posicao')