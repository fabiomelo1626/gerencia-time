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

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Salvar os dados
        self.jogador.cont += 1
        self.jogador.acerto_passe_curto = self.acerto_passe_curto
        self.jogador.media_acert_pass_curt = self.jogador.acerto_passe_curto / self.jogador.cont
        self.jogador.acerto_passe_longo = self.acerto_passe_longo
        self.jogador.media_acert_pass_long = self.jogador.acerto_passe_longo / self.jogador.cont
        self.jogador.gols = self.gols
        self.jogador.media_gosl = self.jogador.gols / self.jogador.cont
        self.jogador.desarmes = self.desarmes
        self.jogador.media_desarmes = self.jogador.desarmes / self.jogador.cont
        self.jogador.defesas = self.defesas
        self.jogador.media_defesas = self.jogador.defesas / self.jogador.cont
        self.jogador.passes_gol = self.passes_gol
        self.jogador.media_pass_gol = self.jogador.passes_gol / self.jogador.cont
        self.jogador.faltas = self.faltas
        self.jogador.media_faltas = self.jogador.faltas / self.jogador.cont
        self.jogador.cartao_amarelo = self.cartao_amarelo
        self.jogador.media_cart_amar = self.jogador.cartao_amarelo / self.jogador.cont
        self.jogador.cartao_vermelho = self.cartao_vermelho
        self.jogador.media_cart_verm = self.jogador.cartao_vermelho / self.jogador.cont
        self.jogador.save()
        super(Scores, self).save(force_insert, force_update, *args, **kwargs)

    def __str__(self):
        return str(self.jogador)
