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
    posicao = models.CharField('Posicao', max_length=17, choices=posicao_choice, default='Goleiro')
    posicao_opcao = models.CharField('Posicao_opcao', null=True, blank=True, max_length=17, choices=posicao_choice)
    cpf = models.CharField('CPF', max_length=14)
    lesoes = models.TextField('Lesões', null=True, blank=True)
    foto = models.ImageField(upload_to='static/img', null=True, blank=True)

    def __str__(self):
        return self.nome
