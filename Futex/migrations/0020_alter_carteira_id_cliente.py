# Generated by Django 4.0.6 on 2022-08-04 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0019_alter_carteira_id_cliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Futex.cliente', verbose_name='Cliente'),
        ),
    ]
