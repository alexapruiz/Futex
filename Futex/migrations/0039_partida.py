# Generated by Django 4.0.6 on 2022-08-15 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0038_cliente_historico_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id_partida', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('id_rodada', models.IntegerField()),
                ('id_time_casa', models.IntegerField()),
                ('id_time_visitante', models.IntegerField()),
                ('placar_time_casa', models.IntegerField()),
                ('placar_time_visitante', models.IntegerField()),
            ],
        ),
    ]
