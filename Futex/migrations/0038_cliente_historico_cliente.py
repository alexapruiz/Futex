# Generated by Django 4.0.6 on 2022-08-08 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0037_alter_carteira_id_cliente_alter_carteira_id_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('endereco', models.CharField(blank=True, max_length=50, null=True)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
        migrations.CreateModel(
            name='Historico_Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.IntegerField()),
                ('id_time', models.IntegerField()),
                ('tipo_operacao', models.IntegerField()),
                ('qtde_acoes', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
    ]