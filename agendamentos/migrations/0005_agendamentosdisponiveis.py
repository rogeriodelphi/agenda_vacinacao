# Generated by Django 3.2.3 on 2022-02-12 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0004_localvacinacao'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentosDisponiveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.TimeField(verbose_name='Horário')),
                ('data', models.DateField()),
                ('num_vagas', models.IntegerField(verbose_name='Número de vagas')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.gruposatendimento', verbose_name='Grupo de Atendimento')),
                ('local_vacinacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.localvacinacao', verbose_name='Local de vacinação')),
                ('vacina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agendamentos.vacina', verbose_name='Vacina')),
            ],
            options={
                'verbose_name': 'Agendamentos Disponíveis',
                'verbose_name_plural': 'Agendamentos Disponíveis',
                'ordering': ['local_vacinacao', 'data', 'horario', '-num_vagas'],
            },
        ),
    ]
