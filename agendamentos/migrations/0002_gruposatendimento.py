# Generated by Django 3.2.3 on 2022-02-12 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GruposAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Digite o nome do grupo de atendimento.', max_length=200)),
                ('idade_minima', models.IntegerField(verbose_name='Idade mínima')),
            ],
            options={
                'verbose_name': 'Grupo de Atendimento',
                'verbose_name_plural': 'Grupos de Atendimento',
                'ordering': ['nome', 'idade_minima'],
            },
        ),
    ]
