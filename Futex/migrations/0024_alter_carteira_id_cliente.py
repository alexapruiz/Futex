# Generated by Django 4.0.6 on 2022-08-04 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Futex', '0023_remove_carteira_id_cliente_carteira_id_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='id_cliente',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
