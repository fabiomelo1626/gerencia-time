from django.db import models
from apps.cadastros.models import *
from django.urls import reverse_lazy


class Scores(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT)
    erro_passe = models.IntegerField('Erros de passes', default=0)
    acerto_passe_curto = models.IntegerField('Passes curtos', default=0)
    acerto_passe_longo = models.IntegerField('Passes longos', default=0)
    gols = models.IntegerField('Gols', default=0)
    desarmes = models.IntegerField('Desarmes', default=0)
    defesas = models.IntegerField('Defesas', default=0)
    passes_gol = models.IntegerField('Passes pra gol', default=0)
    faltas = models.IntegerField('Faltas', default=0)
    cartao_amarelo = models.IntegerField('Cartão Amarelo', default=0)
    cartao_vermelho = models.IntegerField('Cartão vermelho', default=0)
    data = models.DateField('Data')

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Salvar os dados
        self.jogador.partidas += 1
        self.jogador.erro_passe += self.erro_passe
        self.jogador.media_erro_passe = self.jogador.erro_passe / self.jogador.partidas
        self.jogador.acerto_passe_curto += self.acerto_passe_curto
        self.jogador.media_acert_pass_curt = self.jogador.acerto_passe_curto / self.jogador.partidas
        self.jogador.acerto_passe_longo += self.acerto_passe_longo
        self.jogador.media_acert_pass_long = self.jogador.acerto_passe_longo / self.jogador.partidas
        self.jogador.gols += self.gols
        self.jogador.media_gosl = self.jogador.gols / self.jogador.partidas
        self.jogador.desarmes += self.desarmes
        self.jogador.media_desarmes = self.jogador.desarmes / self.jogador.partidas
        self.jogador.defesas += self.defesas
        self.jogador.media_defesas = self.jogador.defesas / self.jogador.partidas
        self.jogador.passes_gol += self.passes_gol
        self.jogador.media_pass_gol = self.jogador.passes_gol / self.jogador.partidas
        self.jogador.faltas += self.faltas
        self.jogador.media_faltas = self.jogador.faltas / self.jogador.partidas
        self.jogador.cartao_amarelo += self.cartao_amarelo
        self.jogador.media_cart_amar = self.jogador.cartao_amarelo / self.jogador.partidas
        self.jogador.cartao_vermelho += self.cartao_vermelho
        self.jogador.media_cart_verm = self.jogador.cartao_vermelho / self.jogador.partidas
        self.jogador.save()
        super(Scores, self).save(force_insert, force_update, *args, **kwargs)

    def __str__(self):
        return str(self.jogador)

    def get_absolute_url(self):
        return reverse_lazy('cadastros:list_jogador')

    class Meta:
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'


class Especifico(models.Model):
    jogador = models.ForeignKey(Jogador, on_delete=models.PROTECT)
    lesoes = models.TextField('Lesões', max_length=400)
    velocidade = models.FloatField('Velocidade', default=0)
    dados_psicologicos = models.TextField('Psicológico', max_length=400)
    dados_nutricionais = models.TextField('Nutricional', max_length=400)

    def __str__(self):
        return str(self.jogador)

    def get_absolute_url(self):
        return reverse_lazy('cadastros:list_jogador')

    class Meta:
        verbose_name = 'Especifico'
        verbose_name_plural = 'Especificos'
