from django.db import models
from apps.cadastros.models import *


class Scores(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT)
    acerto_passe_curto = models.IntegerField('Short_pass', default=0)
    acerto_passe_longo = models.IntegerField('Long_pass', default=0)
    gols = models.IntegerField('Gols', default=0)
    desarmes = models.IntegerField('Desarmes', default=0)
    defesas = models.IntegerField('Defesas', default=0)
    passes_gol = models.IntegerField('Pass_gol', default=0)
    faltas = models.IntegerField('Faltas', default=0)
    cartao_amarelo = models.IntegerField('Yellow_card', default=0)
    cartao_vermelho = models.IntegerField('Red_card', default=0)
    data = models.DateField('Data')

    def __str__(self):
        return str(self.jogador)
