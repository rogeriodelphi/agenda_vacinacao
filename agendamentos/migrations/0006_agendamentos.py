# Generated by Django 3.2.3 on 2022-02-12 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0005_agendamentosdisponiveis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('a', 'Agendado'), ('c', 'Cancelado'), ('v', 'Vacinado')], default='a', help_text='Digite o status do agendamento.', max_length=200, verbose_name='Status do agendamento')),
                ('data_realizado', models.DateField(auto_now_add=True, verbose_name='Realizado na data')),
                ('agendamento_disponivel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.agendamentosdisponiveis', verbose_name='Agendamento')),
                ('cidadao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nome do Cidadão')),
            ],
            options={
                'verbose_name': 'Agendamentos Feitos',
                'verbose_name_plural': 'Agendamentos Feitos',
                'ordering': ['status'],
            },
        ),
    ]
