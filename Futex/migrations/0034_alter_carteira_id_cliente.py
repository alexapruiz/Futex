# Generated by Django 4.0.6 on 2022-08-06 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0033_alter_carteira_id_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='id_cliente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='id_carteira_cliente', to='Futex.cliente'),
        ),
    ]
