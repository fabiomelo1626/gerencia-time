# Generated by Django 3.1.7 on 2021-02-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0005_auto_20210222_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='posicao',
            field=models.CharField(choices=[('La', 'Lateral Direito'), ('Le', 'Lateral Esquerdo'), ('Me', 'Meia Esquerda'), ('Go', 'Goleiro'), ('V', 'Primeiro Volante'), ('Mc', 'Meia Central'), ('Ata_d', 'Atacante Direita'), ('Ce', 'Centroavante'), ('Ata_e', 'Atacante Esquerda'), ('Zd', 'Zagueiro Direito'), ('Md', 'Meia Direita'), ('Vm', 'Segundo Volante'), ('Ze', 'Zagueiro Esquerdo')], default='Goleiro', max_length=17, verbose_name='Posicao'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='posicao_opcao',
            field=models.CharField(blank=True, choices=[('La', 'Lateral Direito'), ('Le', 'Lateral Esquerdo'), ('Me', 'Meia Esquerda'), ('Go', 'Goleiro'), ('V', 'Primeiro Volante'), ('Mc', 'Meia Central'), ('Ata_d', 'Atacante Direita'), ('Ce', 'Centroavante'), ('Ata_e', 'Atacante Esquerda'), ('Zd', 'Zagueiro Direito'), ('Md', 'Meia Direita'), ('Vm', 'Segundo Volante'), ('Ze', 'Zagueiro Esquerdo')], max_length=17, null=True, verbose_name='Posicao_opcao'),
        ),
    ]