# Generated by Django 4.0.6 on 2022-08-05 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0032_alter_time_id_time_alter_time_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carteira',
            name='id_time',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='id_carteira_time', to='Futex.time'),
        ),
    ]
