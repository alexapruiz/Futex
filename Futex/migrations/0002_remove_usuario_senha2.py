# Generated by Django 4.0.6 on 2022-07-19 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Futex', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='senha2',
        ),
    ]
