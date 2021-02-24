from django.db import models


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
    lesoes = models.TextField('Lesões', null=True, blank=True)
    foto = models.ImageField(upload_to='static/img', null=True, blank=True)
    #SCORES
    acerto_passe_curto = models.IntegerField('Short_pass', default=0)
    media_acert_pass_curt = models.FloatField('média_short_pass', default=0)
    acerto_passe_longo = models.IntegerField('Long_pass', default=0)
    media_acert_pass_long = models.FloatField('média_long_pass', default=0)
    gols = models.IntegerField('Gols', default=0)
    media_gols = models.FloatField('média_gols', default=0)
    desarmes = models.IntegerField('Desarmes', default=0)
    media_desarmes = models.FloatField('média_desarmes', default=0)
    defesas = models.IntegerField('Defesas', default=0)
    media_defesas = models.FloatField('média_defesas', default=0)
    passes_gol = models.IntegerField('Pass_gol', default=0)
    media_pass_gol = models.FloatField('média_pass_gol', default=0)
    faltas = models.IntegerField('Faltas', default=0)
    media_faltas = models.FloatField('média_faltas', default=0)
    cartao_amarelo = models.IntegerField('Yellow_card', default=0)
    media_cart_amar = models.FloatField('média_yellow_card', default=0)
    cartao_vermelho = models.IntegerField('Red_card', default=0)
    media_cart_verm = models.FloatField('média_red_card', default=0)
    cont = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.nome, self.posicao)

    class Meta:
        verbose_name = 'Jogador'
        verbose_name_plural = 'Jogadores'
