# Generated by Django 4.0.6 on 2022-08-04 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0031_remove_carteira_id_cliente_carteira_id_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='id_time',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='time',
            name='nome',
            field=models.CharField(max_length=30),
        ),
    ]
