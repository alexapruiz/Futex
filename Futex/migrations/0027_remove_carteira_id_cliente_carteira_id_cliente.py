# Generated by Django 4.0.6 on 2022-08-04 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0026_alter_cliente_id_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carteira',
            name='id_cliente',
        ),
        migrations.AddField(
            model_name='carteira',
            name='id_cliente',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Futex.cliente', verbose_name='Cliente'),
        ),
    ]
