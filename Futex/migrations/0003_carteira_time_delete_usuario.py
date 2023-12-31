# Generated by Django 4.0.6 on 2022-07-19 22:01

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0002_remove_usuario_senha2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usuario', models.IntegerField()),
                ('id_time', models.IntegerField()),
                ('qyde_acoes', models.IntegerField()),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_time', models.IntegerField()),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
