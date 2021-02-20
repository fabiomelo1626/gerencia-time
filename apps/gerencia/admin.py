from django.contrib import admin
from .models import *


@admin.register(Scores)
class ScoresAdmin(admin.ModelAdmin):
    model = Scores
    list_display = ('jogador', 'data')
