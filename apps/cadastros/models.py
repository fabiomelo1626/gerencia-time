from django.db import models
from django.urls import reverse_lazy


class Jogador(models.Model):
    posicao_choice = {
        ('Go', 'Goleiro'),
        ('Le', 'Lateral Esquerdo'),
        ('La', 'Lateral Direito'),
        ('Ze', 'Zagueiro Esquerdo'),
        ('Zd', 'Zagueiro Direito'),
        ('V', 'Primeiro Volante'),
        ('Vm', 'Segundo Volante'),
        ('Me', 'Meia Esquerda'),
        ('Md', 'Meia Direita'),
        ('Mc', 'Meia Central'),
        ('Ata_d', 'Atacante Direita'),
        ('Ata_e', 'Atacante Esquerda'),
        ('Ce', 'Centroavante')
    }
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    posicao = models.CharField('Posicao', max_length=17, choices=posicao_choice, default='')
    posicao_opcao = models.CharField('Posicao_opcao', null=True, blank=True, max_length=17, choices=posicao_choice)
    cpf = models.CharField('CPF', max_length=14)
    foto = models.FileField(upload_to='media/%y/%m/%d/', null=True, blank=True)
    #SCORES
    erro_passe = models.IntegerField('Erros de passes', default=0)
    media_erro_passe = models.FloatField('Média de passes errados', default=0)
    acerto_passe_curto = models.IntegerField('Passes curtos', default=0)
    media_acert_pass_curt = models.FloatField('Média de passes curtos', default=0)
    acerto_passe_longo = models.IntegerField('Passes longos', default=0)
    media_acert_pass_long = models.FloatField('Média de passes longos', default=0)
    gols = models.IntegerField('Gols', default=0)
    media_gols = models.FloatField('Média de gols', default=0)
    desarmes = models.IntegerField('Desarmes', default=0)
    media_desarmes = models.FloatField('Média de desarmes', default=0)
    defesas = models.IntegerField('Defesas', default=0)
    media_defesas = models.FloatField('Média de defesas', default=0)
    passes_gol = models.IntegerField('Passes pra gol', default=0)
    media_pass_gol = models.FloatField('Média de passes pra gol', default=0)
    faltas = models.IntegerField('Faltas', default=0)
    media_faltas = models.FloatField('Média de faltas', default=0)
    cartao_amarelo = models.IntegerField('Cartão Amarelo', default=0)
    media_cart_amar = models.FloatField('Média de cartões amarelos', default=0)
    cartao_vermelho = models.IntegerField('Cartão vermelho', default=0)
    media_cart_verm = models.FloatField('Média de cartões vermelhos', default=0)
    partidas = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.nome, self.posicao)

    def get_absolute_url(self):
        return reverse_lazy('cadastros:list_jogador')

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
