# Generated by Django 4.0.6 on 2022-08-04 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0022_alter_carteira_id_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteira',
            name='id_cliente',
        ),
        migrations.AddField(
            model_name='carteira',
            name='id_cliente',
            field=models.ManyToManyField(to='Futex.cliente'),
        ),
    ]
