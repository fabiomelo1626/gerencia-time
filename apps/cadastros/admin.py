from django.contrib import admin
from .models import *


@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
        model = Jogador
        list_display = ('nome', 'idade', 'posicao')