# Generated by Django 4.0.6 on 2022-08-08 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0035_delete_historico_cliente_rename_id_time_time_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='id',
            new_name='id_time',
        ),
    ]
