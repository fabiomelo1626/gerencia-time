# Generated by Django 3.1.7 on 2021-02-23 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_auto_20210223_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='posicao',
            field=models.CharField(choices=[('La', 'Lateral Direito'), ('Ata_d', 'Atacante Direita'), ('Zd', 'Zagueiro Direito'), ('Me', 'Meia Esquerda'), ('Mc', 'Meia Central'), ('V', 'Primeiro Volante'), ('Ce', 'Centroavante'), ('Le', 'Lateral Esquerdo'), ('Md', 'Meia Direita'), ('Go', 'Goleiro'), ('Ata_e', 'Atacante Esquerda'), ('Ze', 'Zagueiro Esquerdo'), ('Vm', 'Segundo Volante')], default='', max_length=17, verbose_name='Posicao'),
        ),
        migrations.AlterField(
            model_name='jogador',
            name='posicao_opcao',
            field=models.CharField(blank=True, choices=[('La', 'Lateral Direito'), ('Ata_d', 'Atacante Direita'), ('Zd', 'Zagueiro Direito'), ('Me', 'Meia Esquerda'), ('Mc', 'Meia Central'), ('V', 'Primeiro Volante'), ('Ce', 'Centroavante'), ('Le', 'Lateral Esquerdo'), ('Md', 'Meia Direita'), ('Go', 'Goleiro'), ('Ata_e', 'Atacante Esquerda'), ('Ze', 'Zagueiro Esquerdo'), ('Vm', 'Segundo Volante')], max_length=17, null=True, verbose_name='Posicao_opcao'),
        ),
    ]