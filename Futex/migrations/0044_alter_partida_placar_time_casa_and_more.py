# Generated by Django 4.0.6 on 2022-08-18 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0043_remove_parametros_id_parametros_id_parametro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='placar_time_casa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='placar_time_visitante',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
