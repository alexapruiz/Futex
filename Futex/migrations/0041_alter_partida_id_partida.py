# Generated by Django 4.0.6 on 2022-08-16 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0040_alter_partida_id_time_casa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='id_partida',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]